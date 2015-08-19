import re
import csv
import os
excl = {}

exclude = open('accounts.csv','r')
csvex = csv.reader(exclude,delimiter='\t')
for row in csvex:
	excl[row[0]] = int(row[1])
	#excl1[row[0]] = 1

arr = ["BillGates_tweets","timoreilly_tweets","Pogue_tweets","ericschmidt_tweets","waltmossberg_tweets","codinghorror_tweets","martinfowler_tweets","shanselman_tweets","spolsky_tweets","KentBeck_tweets","jack_tweets","masason_tweets","biz_tweets","notch_tweets","elonmusk_tweets","ev_tweets","TEDchris_tweets","Padmasree_tweets","kevinrose_tweets","dickc_tweets","noaheverett_tweets","Ghonim_tweets","om_tweets","kaifulee_tweets","jeb__tweets","tim_cook_tweets","karaswisher_tweets","marissamayer_tweets","MichaelDell_tweets","majornelson_tweets","kenichiromogi_tweets","alaa_tweets","onambiguity_tweets","Chad_Hurley_tweets","leolaporte_tweets","anildash_tweets","SethBling_tweets","Dinnerbone_tweets","mikeyk_tweets","mattcutts_tweets","satyanadella_tweets","saurik_tweets","stevewoz_tweets","johnmaeda_tweets","chadfowler_tweets","john_tweets","ginatrapani_tweets","jbernhardsson_tweets","zeldman_tweets","pod2g_tweets","evad3rs_tweets","finkd_tweets","bgurley_tweets","pmarca_tweets","tnatsu_tweets","DuvalMagic_tweets","rsarver_tweets","reidhoffman_tweets","Fwiz_tweets","durov_tweets","DavidVonderhaar_tweets","Gronkh_tweets","MichaelCondrey_tweets","sivers_tweets","therealcliffyb_tweets","jkottke_tweets","digiphile_tweets","jkalucki_tweets","paulg_tweets","HIDEO_KOJIMA_EN_tweets","iH8sn0w_tweets","ID_AA_Carmack_tweets","nzkoz_tweets","myspacetom_tweets","abdur_tweets","carlmanneh_tweets","bs_tweets","todsacerdoti_tweets","timberners_lee_tweets","mollstam_tweets","_tomcc_tweets","Kappische_tweets","vpieters_tweets","jeresig_tweets","JahKob_tweets","p0sixninja_tweets","danfrisk_tweets","bhorowitz_tweets","noobde_tweets","minliangtan_tweets","cdixon_tweets","Benioff_tweets","IGLevine_tweets","paul_irish_tweets","srlm_tweets","robhoward_tweets","pschiller_tweets","tconrad_tweets","jonkagstrom_tweets","preillyme_tweets","demandrichard_tweets","levie_tweets","dongatory_tweets","_grum_tweets","mezzoblue_tweets",
"a_tweets",
"dhh_tweets",
"shoemoney_tweets",
"pierre_tweets",
"JD_2020_tweets",
"rkmt_tweets",
"e_kaspersky_tweets",
"joebelfiore_tweets",
"i0n1c_tweets",
"KrisJelbring_tweets",
"chriscoyier_tweets",
"sundarpichai_tweets",
"xlson_tweets",
"jemimakiss_tweets",
"RiotPendragon_tweets",
"lukew_tweets",
"carnalizer_tweets",
"drewhouston_tweets",
"ZacheryNielson_tweets",
"paulsingh_tweets",
"austinnotduncan_tweets",
"scottgu_tweets",
"chpwn_tweets",
"RamyRaoof_tweets",
"jimmy_wales_tweets",
"JonCrawford_tweets",
"zephoria_tweets",
"rocket2guns_tweets",
"LoaiNagati_tweets",
"ZeinabSamir_tweets",
"Joi_tweets",
"pmolyneux_tweets",
"l2k_tweets",
"sorenmacbeth_tweets",
"mkapor_tweets",
"sarahcuda_tweets",
"anamitra_tweets",
"addyosmani_tweets",
"akirareiko_tweets",
"wol_lay_tweets",
"skonnard_tweets",
"jsa_tweets",
"AquaXetine_tweets",
"f_tweets",
"Swiftor_tweets",
"DaveSumter_tweets",
"RanaASaid_tweets",
"AkihiroHino_tweets",
"habibh_tweets",
"ChrisMetzen_tweets",
"gr33ndata_tweets",
"simplebits_tweets",
"andrewchen_tweets",
"EdmundMcMillenn_tweets",
"stanleytang_tweets",
"meyerweb_tweets",
"BomuBoi_tweets",
"ryan_tweets",
"Harada_TEKKEN_tweets",
"marcoarment_tweets",
"tha_rami_tweets",
"sama_tweets",
"willsmith_tweets",
"reckless_tweets",
"br_tweets",
"travisk_tweets",
"larryellison_tweets",
"harrymccracken_tweets",
"EvilSeph_tweets",
"ibogost_tweets",
"jeff_tweets",
"fart_tweets",
"photomatt_tweets",
"dens_tweets",
"Arubin_tweets",
"j_smedley_tweets",
"SamFURUKAWA_tweets",
"PG_kamiya_tweets",
"scottebales_tweets",
"aaronwall_tweets",
"chrismessina_tweets",
"tinyBuild_tweets",
"Jonathan_Blow_tweets",
"kevin_tweets",
"Goldman44_tweets",
"stephenlrose_tweets",
"pgeuder_tweets",
"JeremyCMorgan_tweets",
"Pentadact_tweets",
"t_tweets",
"Werner_tweets",
"tanakaryusaku_tweets",
"beep_tweets",
"chrisremo_tweets",
"petecashmore_tweets"	
]

for i in range(0,200):
	userfname = os.path.join('tweets', str(arr[i]) + '.csv')
	with open (userfname, "r") as myfile:
   		data=myfile.read()
    		data = re.sub('[:,!.")(\']+','',data)
    	#print re.findall(r"#(\w+)", data)
	f = open('accounts.csv', "wb")

	for i in data.split():
		if i.startswith("@"):
			if not excl.has_key(i):
				excl[i] = 1
			else:	
				excl[i] = excl[i] + 1


	for key in excl:	
		params = (key,excl[key])
		f.write('%s\t%s\n' % params)

