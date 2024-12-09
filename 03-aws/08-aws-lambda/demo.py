def lambda_handler(event, context):
    # Print a message to the logs
    print("Hello from AWS Lambda!")
    
    # Return a response
    return {
        'statusCode': 200,
        'body': 'Message printed successfully!'
    }
