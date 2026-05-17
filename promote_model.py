from mlflow.tracking import MlflowClient

client = MlflowClient()

client.set_registered_model_alias(
    name="rakuten_model",
    alias="prod",
    version=7
)

print("✅ Model assigned to alias 'prod'")
