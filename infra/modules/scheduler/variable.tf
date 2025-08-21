variable "aws_lambda_arn" {
    description = "Arn da AWS que Rodara no Event"
    type = string
}

variable "aws_role_arn_scheduler" {
    description = "Arn da Role que sera adicionada ao scheduler"
    type = string
}
