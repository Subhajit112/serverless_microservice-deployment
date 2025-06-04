output "api_invoke_url" {
  value = "${aws_api_gateway_rest_api.user_api.execution_arn}/users"
}
