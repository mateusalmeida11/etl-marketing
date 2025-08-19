
resource "aws_s3_bucket" "bucket_etl_marketing" {
    bucket = var.s3_bucket_marketing

    tags = {
        Name = "BucketDataLake",
        Environment = "Dev"
    }
}

resource "aws_s3_bucket_public_access_block" "bucket_etl_marketing_public_access_block" {
    bucket = var.s3_bucket_marketing

    block_public_acls = true
    block_public_policy = true
    ignore_public_acls = true
    restrict_public_buckets = true
}
