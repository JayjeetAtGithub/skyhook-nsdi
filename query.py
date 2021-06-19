projection = {
    "vendor_id_renamed": ds.field("VendorID"),
    "total_amount_more_than_27": ds.field("total_amount") > 27,
    "payment_type_2": ds.field("payment_type") == 2
}
