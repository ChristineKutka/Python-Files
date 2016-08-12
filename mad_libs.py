level = input("""Instructions
	If you want to play easy Mad libs type one.
	If you want to play medium Mad libs type two.
	If you want to play hard Mad libs type three.""")

if level == int("1") :
	adj_1 = input("Give me an adjective.")
	adj_2 = input("Give me an adjective.")
	pn_1 = input("Give me a plural noun.")
	print ("Ladies and gentlemen, on this " 
		+  adj_1
		+ " occasion it is a privilege to address such a/an "
		+  adj_2
		+ "-looking group of " 
		+  pn_1)  
elif level == 2:
	adj_1 = input("Give me an adjective.")
	adj_2 = input("Give me an adjective.")
	pn_1 = input("Give me a plural noun.")
	pn_2 = input("Give me a plural noun.")
	adj_3 = input("Give me an adjective.")
	n_1 = input("Give me a noun.")
	n_2 = input("Give me a noun.")
	pn_3 = input("Give me a plural noun.")
	adj_4 = input("Give me an adjective.")
	guy_name_1 = input("Give me a guy name.")
	adj_5 = input("Give me an adjective.")
	n_3 = input("Give me a noun.")
	print ("Ladies and gentlemen, on this " 
		+  adj_1
		+ " occasion it is a privilege to address such a/an "
		+  adj_2
		+ "-looking group of "
		+  pn_1  
		+ " I can tell from your smiling "
		+  pn_2 
		+ " that you will support my "
		+ adj_3
		+ " program in the coming election. I promise that, if elected, there will be a/an "
		+ n_1
		+ " in every "
		+ n_2
		+ " and two "
		+ pn_3
		+ " in every garage. I want to warn you against my" 
		+ adj_4
		+ " opponent. Mr. "
		+ guy_name_1
		+ " The man is nothing but a/an "
		+ adj_5
		+ n_3) 
elif level == 3: 
	adj_1 = input("Give me an adjective.")
	adj_2 = input("Give me an adjective.")
	pn_1 = input("Give me a plural noun.")
	pn_2 = input("Give me a plural noun.")
	adj_3 = input("Give me an adjective.")
	n_1 = input("Give me a noun.")
	n_2 = input("Give me a noun.")
	pn_3 = input("Give me a plural noun.")
	adj_4 = input("Give me an adjective.")
	guy_name_1 = input("Give me a guy name.")
	adj_5 = input("Give me an adjective.")
	n_3 = input("Give me a noun.")
	adj_6 = input("Give me an adjective.")
	n_4 = input("Give me a noun.")
	pn_4 = input("Give me a plural noun.")
	pn_5 = input("Give me a plural noun.")
	adj_7 = input("Give me an adjective.")
	adj_8 = input("Give me an adjective.")
	adj_9 = input("Give me an adjective.")
	print ("Ladies and gentlemen, on this " 
		+  adj_1
		+ " occasion it is a privilege to address such a/an "
		+  adj_2
		+ "-looking group of "
		+  pn_1  
		+ " I can tell from your smiling "
		+  pn_2 
		+ " that you will support my "
		+ adj_3
		+ " program in the coming election. I promise that, if elected, there will be a/an "
		+ n_1
		+ " in every "
		+ n_2
		+ " and two "
		+ pn_3
		+ " in every garage. I want to warn you against my" 
		+ adj_4
		+ " opponent. Mr. "
		+ guy_name_1
		+ " The man is nothing but a/an "
		+ adj_5
		+ n_3
		+ ". He has a/an"
		+ adj_6
		+ " character and is working "
		+ n_4
		+ " in glove with the criminal element. If elected, I promise to eliminate vice. I will keep the "
		+ pn_4
		+ " off the city's streets. I will keep crooks from dipping their " 
		+ pn_5
		+ " in the public till. "
		+ adj_6
		+ " I promise you "
		+ adj_7
		+ " government. "
		+ adj_8
		+ " taxes, and "
		+ adj_9
		+ " schools. "
	)
