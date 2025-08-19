resource "aws_lambda_function" "lambda_etl" {
    function_name = var.aws_lambda_name_layer
    role = var.arn_policy_lambda_execution
    package_type = "Image"
    image_uri = "${var.url_repos_etl_marketing}:{$var.image_tag}

    logging_config {
        log_format = "JSON"
    }
}
