import os

# --- Main Handler ---
def lambda_handler(event, context):
  """
  Route the incoming request based on intent.
  The JSON body of the request is provided in the event slot.
  """

  print(event)

  intent_name = event['sessionState']['intent']['name']
  fn_name = os.environ.get(intent_name)
  print(f"Intent: {intent_name} -> Lambda: {fn_name}")
