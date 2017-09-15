resource "aws_security_group" "portchange_slingr_test_truetag" {
  name = "portchange_slingr_test_truetag"
  tags = "${var.default_tags_true_tag}"
}
