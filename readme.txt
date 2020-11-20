Karabiner is a keyboard remapping utility. With Karabiner running on your computer, you can press one key on your keyboard and get a different output. For example, you could remap \ to = , or make change a QWERTY keyboard to dvorak or another layout.

If there are a lot of remappings, it could be tedious to select them all manually in karabiner. With a csv, you can easily create and edit a table of key remappings.

See csv_instructions.txt for how to build a csv file.

After saving the .csv and running csv_to_json.py, open karabiner and create a new profile. Under the complex modifications tab, click Add rule. The rules created in your csv should show up in the list, along with an Enable All option.