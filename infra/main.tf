module "ecr" {
    source = "./modules/ecr"
}

module "s3" {
    source = "./modules/s3"
}

module "iam" {
    source = "./modules/policies"
    bucket_s3_etl_arn = module.s3.root_path_bucket_s3,
    aws_lambda_arn= module.lambda.aws_lambda_arn
}

module "lambda" {
    source = "./modules/lambda"
    url_repos_etl_marketing=module.ecr.ecr_repositor_url
    image_tag = var.image_tag
    arn_policy_lambda_execution = module.iam.lambda_execution_role_arn
}

module "scheduler" {
    source = "./modules/scheduler"
    aws_role_arn_scheduler = module.iam.aws_scheduler_execution_role_arn
    aws_lambda_arn = module.lambda.aws_lambda_arn
}
