{
    SchemaConfigRoot: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType("Element")
        ]
    },
    "Element": {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey("Name", "Class", "Parent")
        ]
    },
    "Name": {
        SchemaType: SchemaTypeString
    },
    "Class": {
        SchemaType: SchemaTypeString
    },
    "Parent": {
        SchemaType: SchemaTypeString
    },
    "SchemaRule": {
        SchemaType: SchemaTypeString
    }
}
