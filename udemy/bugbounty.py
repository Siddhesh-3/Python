import requests
import stripe
charge = stripe.Charge.retrieve(
  "ch_1ITWro2eZvKYlo2CF1czqnNj",
  api_key="pk_live_UCgFiuZoBEszAPxWJDr6DEyN00E5eQGOXH"
)
charge.save() # Uses the same API Key.