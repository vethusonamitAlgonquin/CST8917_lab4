import os
from dotenv import load_dotenv
import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage

load_dotenv()
# Azure Service Bus connection string
CONNECTION_STR = os.getenv("SERVICE_BUS_CONNECTION_STR")
QUEUE_NAME = "booking-requests"

def submit_booking(booking_details):
    
    try:
        # Create a ServiceBusClient using the connection string
        servicebus_client = ServiceBusClient.from_connection_string(CONNECTION_STR)

        # Create a ServiceBusSender object
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)

        # Serialize the dictionary to JSON
        message_body = json.dumps(booking_details)

        # Create a message
        message = ServiceBusMessage(message_body)

        # Send the message to the queue
        with sender:
            sender.send_messages(message)
        print("Booking request submitted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        

if __name__ == "__main__":
    # Example booking details
    booking = {
        "user_id": "12345",
        "user_email": "vethusonamit@gmail.com",
        "booking_date": "2024-04-03",
        "booking_details": "This is a test booking."
    }

    # Submit the booking
    submit_booking(booking)
