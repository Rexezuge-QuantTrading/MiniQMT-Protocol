from miniqmt_protocol import OrderRequest, StylePayload


def test_order_request_round_trips_json():
    request = OrderRequest(
        account_id="1000000365",
        client_order_id="jq123",
        strategy_id="demo",
        method="order_target_value",
        security="000001.XSHE",
        target_value=1000,
        style=StylePayload(type="market"),
    )

    payload = request.model_dump()

    assert payload["method"] == "order_target_value"
    assert payload["style"]["type"] == "market"
