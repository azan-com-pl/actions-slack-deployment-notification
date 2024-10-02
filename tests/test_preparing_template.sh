render_template() {
  (cd .. && ENV_JSON="tests/inputs/$1" python3 render_template.py notification.json.j2)
}

assert_equals_jq() {
  actual=$(echo "$1" | jq -r "$2")
  expected=$3

  assert_equals "$expected" "$actual"
}

test_building_template_pwa() {
  output=$(render_template "preparing-pwa.json")

  assert_equals_jq "$output" '.text' "PWA build has been triggered by *@octocat* :tractor:, will be deployed to *test*"
}

test_building_template_magento() {
  output=$(render_template "preparing-magento.json")

  assert_equals_jq "$output" '.text' "Magento build has been triggered by *@octocat* :tractor:, will be deployed to *test*"
}
