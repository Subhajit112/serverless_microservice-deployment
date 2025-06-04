resource "aws_dynamodb_table" "user_profiles" {
  name           = var.dynamodb_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "userId"

  attribute {
    name = "userId"
    type = "S"
  }

  tags = {
    Environment = var.environment
  }
}
