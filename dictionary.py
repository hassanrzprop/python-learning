bike={
    "name":"GS 150",
    "model":'2022',
    "company":"Suzuki",
    "color":"Black"
}
# dictionary data read  methods
print(bike["name"])
print(bike.get("color",{}))

# dictionary data update method
bike["model"]="2024"
print(bike)


# dictionary data add
bike["EngineCC"]="150"
print(bike)

# dictionary data delete
del bike["color"]
bike.pop("EngineCC")
# popitem to delete last one
bike.popitem()
print(bike)