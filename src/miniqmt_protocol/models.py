"""Versioned MiniQMT HTTP protocol models."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

ProtocolVersion = Literal["v1"]
OrderMethod = Literal["order", "order_target", "order_value", "order_target_value"]
OrderStatus = Literal["submitted", "filled", "partial", "cancelled", "rejected", "unknown"]
OrderSide = Literal["long"]


class StylePayload(BaseModel):
    type: Literal["market", "limit"] = "market"
    price: float | None = None


class HealthResponse(BaseModel):
    status: Literal["ok", "degraded"] = "ok"
    version: ProtocolVersion = "v1"
    miniqmt_connected: bool = False
    trading_enabled: bool = False


class PositionPayload(BaseModel):
    security: str
    total_amount: int = 0
    closeable_amount: int = 0
    price: float = 0.0
    avg_cost: float = 0.0
    value: float = 0.0


class PortfolioResponse(BaseModel):
    account_id: str
    account_type: str = "STOCK"
    available_cash: float = 0.0
    frozen_cash: float = 0.0
    market_value: float = 0.0
    total_asset: float = 0.0
    positions: list[PositionPayload] = Field(default_factory=list)


class OrderRequest(BaseModel):
    account_id: str
    account_type: str = "STOCK"
    client_order_id: str
    strategy_id: str
    method: OrderMethod
    security: str
    style: StylePayload = Field(default_factory=StylePayload)
    side: OrderSide = "long"
    pindex: int = 0
    close_today: bool = False
    amount: int | None = None
    value: float | None = None
    target_amount: int | None = None
    target_value: float | None = None


class OrderResponse(BaseModel):
    client_order_id: str
    broker_order_id: str | None = None
    security: str
    amount: int = 0
    filled_amount: int = 0
    price: float = 0.0
    value: float = 0.0
    commission: float = 0.0
    status: OrderStatus = "submitted"
    reason: str | None = None


class HistoryRequest(BaseModel):
    security: str
    count: int
    unit: str = "1d"
    fields: list[str] = Field(default_factory=lambda: ["open", "close", "high", "low", "volume", "money"])
    skip_paused: bool = True
    fq: Literal["pre", "post"] | None = "pre"


class PriceRequest(BaseModel):
    securities: list[str]
    start_date: str | None = None
    end_date: str | None = None
    frequency: str = "daily"
    fields: list[str] = Field(default_factory=lambda: ["open", "close", "high", "low", "volume", "money"])
    skip_paused: bool = False
    fq: Literal["pre", "post"] | None = "pre"
    count: int | None = None
    fill_paused: bool = True


class BarPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    datetime: str


class HistoryResponse(BaseModel):
    security: str
    rows: list[BarPayload] = Field(default_factory=list)


class PriceSecurityPayload(BaseModel):
    security: str
    rows: list[BarPayload] = Field(default_factory=list)


class PriceResponse(BaseModel):
    securities: list[PriceSecurityPayload] = Field(default_factory=list)


class CurrentRequest(BaseModel):
    securities: list[str]


class CurrentDataPayload(BaseModel):
    security: str
    paused: bool = False
    last_price: float | None = None
    high_limit: float | None = None
    low_limit: float | None = None
    is_st: bool | None = None
    day_open: float | None = None
    name: str | None = None
    industry_code: str | None = None


class CurrentResponse(BaseModel):
    current: list[CurrentDataPayload] = Field(default_factory=list)


class TradeDaysRequest(BaseModel):
    start_date: str | None = None
    end_date: str | None = None
    count: int | None = None


class TradeDaysResponse(BaseModel):
    days: list[str] = Field(default_factory=list)


class SecurityInfoRequest(BaseModel):
    code: str


class SecurityInfoPayload(BaseModel):
    code: str
    display_name: str | None = None
    name: str | None = None
    start_date: Any = None
    end_date: Any = None
    type: str | None = None


class SecurityInfoResponse(BaseModel):
    security: SecurityInfoPayload


class IndexStocksRequest(BaseModel):
    index_symbol: str
    date: str | None = None


class IndexStocksResponse(BaseModel):
    securities: list[str] = Field(default_factory=list)
