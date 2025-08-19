module "ecr" {
    source = "./modules/ecr"
}

module "s3" {
    source = "./modules/s3"
}

module "iam" {
    soruce = "./modules/policies"
    bucket_s3_etl_arn = module.ecr.root_path_bucket_s3
}

module "lambda" {
    source = "./modules/lambda"
    url_repos_etl_marketing=module.ecr.ecr_repositor_url
    image_tag = var.image_tag
    arn_policy_lambda_execution = module.iam.lambda_execution_role_arn
}
