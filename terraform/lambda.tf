resource "aws_lambda_function" "user_profile_lambda" {
  function_name = "${var.project_name}_lambda"
  filename      = "../lambda_function_payload.zip"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "user_handler.handler"
  runtime       = "python3.9"
  timeout       = 15

  environment {
    variables = {
      DYNAMODB_TABLE = aws_dynamodb_table.user_profiles.name
    }
  }

  source_code_hash = filebase64sha256("../lambda_function_payload.zip")
}
