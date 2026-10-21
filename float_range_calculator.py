def find_exterior_float_intersects(roll):
    # factory new
    
    if not (roll["r"] < 0 or roll["l"] > 0.07):
        fn_l = max(roll["l"], 0)
        fn_r = min(roll["r"], 0.07)
        
        fn_size = fn_r - fn_l
        
        roll["fn_prob"] = fn_size / roll["size"]
        
    # minimal wear
    
    if not (roll["r"] < 0.07 or roll["l"] > 0.15):
        mw_l = max(roll["l"], 0.07)
        mw_r = min(roll["r"], 0.15)
        
        mw_size = mw_r - mw_l
        
        roll["mw_prob"] = mw_size / roll["size"]
        
    # field-tested
    
    if not (roll["r"] < 0.15 or roll["l"] > 0.38):
        ft_l = max(roll["l"], 0.15)
        ft_r = min(roll["r"], 0.38)
        
        ft_size = ft_r - ft_l
        
        roll["ft_prob"] = ft_size / roll["size"]
        
    # well-worn
    
    if not (roll["r"] < 0.38 or roll["l"] > 0.45):
        ww_l = max(roll["l"], 0.38)
        ww_r = min(roll["r"], 0.45)
        
        ww_size = ww_r - ww_l
        
        roll["ww_prob"] = ww_size / roll["size"]
        
    # battle-scarred
    
    if not (roll["r"] < 0.45 or roll["l"] > 1):
        bs_l = max(roll["l"], 0.45)
        bs_r = min(roll["r"], 1)
        
        bs_size = bs_r - bs_l
        
        roll["bs_prob"] = bs_size / roll["size"]

l = float(input("Enter the minimum float value for the skin: "))
r = float(input("Enter the maximum float value for the skin: "))

fn_roll = {"l" : l + 0 * (r - l),
           "r" : l + 0.07 * (r - l), 
           "size" : (l + 0.07 * (r - l)) - (l + 0 * (r - l)), 
           "fn_prob" : 0, "mw_prob" : 0, "ft_prob" : 0, "ww_prob" : 0, "bs_prob" : 0}
mw_roll = {"l" : l + 0.08 * (r - l),
           "r" : l + 0.15 * (r - l), 
           "size" : (l + 0.15 * (r - l)) - (l + 0.08 * (r - l)),
           "fn_prob" : 0, "mw_prob" : 0, "ft_prob" : 0, "ww_prob" : 0, "bs_prob" : 0}
ft_roll = {"l" : l + 0.16 * (r - l),
           "r" : l + 0.38 * (r - l), 
           "size" : (l + 0.38 * (r - l)) - (l + 0.16 * (r - l)),
           "fn_prob" : 0, "mw_prob" : 0, "ft_prob" : 0, "ww_prob" : 0, "bs_prob" : 0}
ww_roll = {"l" : l + 0.39 * (r - l),
           "r" : l + 0.45 * (r - l), 
           "size" : (l + 0.45 * (r - l)) - (l + 0.39 * (r - l)),
           "fn_prob" : 0, "mw_prob" : 0, "ft_prob" : 0, "ww_prob" : 0, "bs_prob" : 0}
bs_roll = {"l" : l + 0.46 * (r - l),
           "r" : l + 1 * (r - l), 
           "size" : (l + 1 * (r - l)) - (l + 0.46 * (r - l)),
           "fn_prob" : 0, "mw_prob" : 0, "ft_prob" : 0, "ww_prob" : 0, "bs_prob" : 0}

# for each skin float interval, check intersection with each wear exterior range
find_exterior_float_intersects(fn_roll)
find_exterior_float_intersects(mw_roll)
find_exterior_float_intersects(ft_roll)
find_exterior_float_intersects(ww_roll)
find_exterior_float_intersects(bs_roll)

total_fn_prob = 0.03 * fn_roll["fn_prob"] + 0.24 * mw_roll["fn_prob"] + 0.33 * ft_roll["fn_prob"] + 0.24 * ww_roll["fn_prob"] + 0.16 * bs_roll["fn_prob"]
total_mw_prob = 0.03 * fn_roll["mw_prob"] + 0.24 * mw_roll["mw_prob"] + 0.33 * ft_roll["mw_prob"] + 0.24 * ww_roll["mw_prob"] + 0.16 * bs_roll["mw_prob"]
total_ft_prob = 0.03 * fn_roll["ft_prob"] + 0.24 * mw_roll["ft_prob"] + 0.33 * ft_roll["ft_prob"] + 0.24 * ww_roll["ft_prob"] + 0.16 * bs_roll["ft_prob"]
total_ww_prob = 0.03 * fn_roll["ww_prob"] + 0.24 * mw_roll["ww_prob"] + 0.33 * ft_roll["ww_prob"] + 0.24 * ww_roll["ww_prob"] + 0.16 * bs_roll["ww_prob"]
total_bs_prob = 0.03 * fn_roll["bs_prob"] + 0.24 * mw_roll["bs_prob"] + 0.33 * ft_roll["bs_prob"] + 0.24 * ww_roll["bs_prob"] + 0.16 * bs_roll["bs_prob"]

print()
print("Factory New Roll: " + str(fn_roll["l"]) + " - " + str(fn_roll["r"]))
print("Minimal Wear Roll: " + str(mw_roll["l"]) + " - " + str(mw_roll["r"]))
print("Field-Tested Roll: " + str(ft_roll["l"]) + " - " + str(ft_roll["r"]))
print("Well-Worn Roll: " + str(ww_roll["l"]) + " - " + str(ww_roll["r"]))
print("Battle-Scarred Roll: " + str(bs_roll["l"]) + " - " + str(bs_roll["r"]))
print()
print("Factory New Odds: " + str(total_fn_prob * 100) + "%")
print("Minimal Wear Odds: " + str(total_mw_prob * 100) + "%")
print("Field-Tested Odds: " + str(total_ft_prob * 100) + "%")
print("Well-Worn Odds: " + str(total_ww_prob * 100) + "%")
print("Battle-Scarred Odds: " + str(total_bs_prob * 100) + "%")