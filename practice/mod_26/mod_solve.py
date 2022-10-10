input_str = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
res_str = ""

a_ord = ord('a')
cap_ord = ord('A')
for c in input_str:
	if c.isalpha():
		num = ord(c)
		rel_ord = a_ord if c.islower() else cap_ord
		new_char = chr(((num - rel_ord + 13) % 26) + rel_ord)

		res_str = res_str + new_char
	else:
		res_str = res_str + c

print(res_str)
