variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "user_profile_service"
}

variable "dynamodb_table_name" {
  type    = string
  default = "UserProfiles"
}

variable "environment" {
  type    = string
  default = "dev"
}
