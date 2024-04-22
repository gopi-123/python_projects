####### Usage of lambda and filters #######


print("Try programiz.pro")
 # Output: '/exp2/ssh2.tgz'
 
dict1 = {
    "WRL6": {"patch": "/exp/wire.tgz", "release": ["NXE"]},
    "RHE8": {"patch": "/exp2/ssh2.tgz", "release": ["EXE"]}
}

release_input = "EXE"

get_patch_for_release = lambda release: dict1[release]["patch"] if release in dict1 and release_input in dict1[release]["release"] else None

patch_value = get_patch_for_release("RHE8")
print(patch_value)  # Output: '/exp2/ssh2.tgz'


####################3 
## Example 2: Using filer and lambda --useful for lists ###########
dict1 = {
    "WRL6": {"patch": "/exp/wire.tgz", "release": ["NXE"]},
    "RHE8": {"patch": "/exp2/ssh2.tgz", "release": ["EXE"]}
}

release_input = "EXE"

filtered_items = filter(lambda item: release_input in item[1]["release"], dict1.items())

#print("filtered_items:",list(filtered_items))
patch_value = next(filtered_items, None)

if patch_value:
    print(patch_value[1]["patch"])  # Output: '/exp2/ssh2.tgz'
else:
    print("No patch found for the specified release.")


############33

## Solution 3: ####### Dict comprehension #############
    
dict1 = {
    "WRL6": {"patch": "/exp/wire.tgz", "release": ["NXE"]},
    "RHE8": {"patch": "/exp2/ssh2.tgz", "release": ["EXE"]}
}

release_input = "EXE"

filtered_items = {key: value for key, value in dict1.items() if release_input in value["release"]}
patch_value = next(iter(filtered_items.values()), {}).get("patch")

print(patch_value)  # Output: '/exp2/ssh2.tgz'

