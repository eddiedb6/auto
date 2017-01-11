{
    SchemaConfigRoot: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType("Key")
        ]
    },
    "Key": {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey("Name", "SchemaType")
        ]
    },
    "Name": {
        SchemaType: SchemaTypeString
    },
    "SchemaType": {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(["SchemaTypeString", "SchemaTypeArray", "SchemaTypeDict", "SchemaTypeInteger"])
        ]
    },
    "SchemaRule": {
        SchemaType: SchemaTypeString
    }
}
