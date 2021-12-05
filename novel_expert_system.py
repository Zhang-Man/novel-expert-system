# _*_ coding:utf-8 _*_
from pyknow import *

novel_list = []
novel_features = []
feature_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global novel_list,novel_features,feature_map,d_desc_map,d_treatment_map
	# 小说列表
	novel = open("novel.txt",encoding='UTF-8')
	novel_t = novel.read()
	novel_list = novel_t.split("\n")
	novel.close()
	# 小说知识库
	for novel in novel_list:
		# 获取小说特征
		novel_s_file = open("Novel features/" + novel + ".txt",encoding='UTF-8')
		novel_s_data = novel_s_file.read()
		s_list = novel_s_data.split("\n")
		novel_features.append(s_list)
		feature_map[str(s_list)] = novel
		novel_s_file.close()
		# 获取小说描述
		novel_s_file = open("Novel descriptions/" + novel + ".txt",encoding='UTF-8')
		novel_s_data = novel_s_file.read()
		d_desc_map[novel] = novel_s_data
		novel_s_file.close()
		# 给出其他相似小说
		novel_s_file = open("Novel Other Choice/" + novel + ".txt",encoding='UTF-8')
		novel_s_data = novel_s_file.read()
		d_treatment_map[novel] = novel_s_data
		novel_s_file.close()
	

def identify_novel(*arguments):
	feature_list = []
	for feature in arguments:
		feature_list.append(feature)
	# Handle key error
	return feature_map[str(feature_list)]

def get_details(novel):
	return d_desc_map[novel]

def get_treatments(novel):
	return d_treatment_map[novel]

def if_not_matched(novel):
		print("")
		id_novel = novel
		novel_details = get_details(id_novel)
		treatments = get_treatments(id_novel)
		print("")
		print("The most probable novel that you have is %s\n" %(id_novel))
		print("A short description of the novel is given below :\n")
		print(novel_details+"\n")
		print("下面也会给你一部分与你想法相似的其他小说: \n")
		print(treatments+"\n")

# @my_decorator
# is just a way of saying just_some_function = my_decorator(just_some_function)
# 辨别疾病的症状有以下几种：头痛，背痛，胸痛，咳嗽，发热，喉咙疼，晕倒，疲惫，低温
#def  identify_novel(fantasy, kungfu, bizarre, Metropolis, powerful, twoD, Immortal, sciencefiction,onlinegames ,military,history):
class NovelF(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("你好！ 我是Zeman，我是来帮助推荐小说的。")
		print("为此，您必须回答一些有关您的条件 输入 yes or no即可，请不要输入其他内容")
		print("您是否有以下想法：")
		print("")
		yield Fact(action="find_novel")


	@Rule(Fact(action='find_novel'), NOT(Fact(fantasy=W())),salience = 1)
	def feature_0(self):
		self.declare(Fact(fantasy=input("玄幻 : ")))

	@Rule(Fact(action='find_novel'), NOT(Fact(kungfu=W())),salience = 1)
	def feature_1(self):
		self.declare(Fact(kungfu=input("武侠: ")))

	@Rule(Fact(action='find_novel'), NOT(Fact(bizarre=W())),salience = 1)
	def feature_2(self):
		self.declare(Fact(bizarre=input("奇幻: ")))

	@Rule(Fact(action='find_novel'), NOT(Fact(Metropolis=W())),salience = 1)
	def feature_3(self):
		self.declare(Fact(Metropolis=input("都市: ")))

	@Rule(Fact(action='find_novel'), NOT(Fact(powerful=W())),salience = 1)
	def feature_4(self):
		self.declare(Fact(powerful=input("异能: ")))

	@Rule(Fact(action='find_novel'), NOT(Fact(Immortal=W())),salience = 1)
	def feature_5(self):
		self.declare(Fact(Immortal=input("仙侠: ")))
	 
	@Rule(Fact(action='find_novel'), NOT(Fact(history=W())),salience = 1)
	def feature_6(self):
		self.declare(Fact(history=input("历史架空: ")))
	
	@Rule(Fact(action='find_novel'), NOT(Fact(onlinegames=W())),salience = 1)
	def feature_7(self):
		self.declare(Fact(onlinegames=input("网游: ")))
	
	@Rule(Fact(action='find_novel'), NOT(Fact(sciencefiction=W())),salience = 1)
	def feature_8(self):
		self.declare(Fact(sciencefiction=input("科幻: ")))
	
	@Rule(Fact(action='find_novel'), NOT(Fact(twoD=W())),salience = 1)
	def feature_9(self):
		self.declare(Fact(twoD=input("二次元: ")))
	
	@Rule(Fact(action='find_novel'), NOT(Fact(military=W())),salience = 1)
	def feature_10(self):
		self.declare(Fact(military=input("军事: ")))

	@Rule(Fact(action='find_novel'), NOT(Fact(Supernatural=W())),salience = 1)
	def feature_11(self):
		self.declare(Fact(Supernatural=input("灵异: ")))

	@Rule(Fact(action='find_novel'), NOT(Fact(Competitive=W())),salience = 1)
	def feature_12(self):
		self.declare(Fact(Competitive=input("竞技: ")))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="yes"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="yes"))
	def novel_0(self):
		self.declare(Fact(novel="诡秘世界之旅"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="yes"),Fact(bizarre="yes"),Fact(Metropolis="no"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="yes"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="no"))
	def novel_1(self):
		self.declare(Fact(novel="江湖位面小人物"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="yes"),Fact(bizarre="yes"),Fact(Metropolis="yes"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_2(self):
		self.declare(Fact(novel="黎明医生"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="no"),Fact(bizarre="yes"),Fact(Metropolis="yes"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_3(self):
		self.declare(Fact(novel="驱魔人的自我修养"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="yes"),Fact(bizarre="yes"),Fact(Metropolis="no"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="yes"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_4(self):
		self.declare(Fact(novel="退后让为师来"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="no"),Fact(bizarre="yes"),Fact(Metropolis="yes"),Fact(powerful="yes"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="yes"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_5(self):
		self.declare(Fact(novel="我的一天有48小时"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="yes"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_6(self):
		self.declare(Fact(novel="我用木雕记录异常"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="no"),Fact(bizarre="yes"),Fact(Metropolis="no"),Fact(powerful="yes"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="no"))
	def novel_7(self):
		self.declare(Fact(novel="我有一座冒险屋"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="yes"))
	def novel_8(self):
		self.declare(Fact(novel="凶案现场直播"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="yes"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="yes"))
	def novel_9(self):
		self.declare(Fact(novel="影视世界当神探"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="yes"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="no"))
	def novel_10(self):
		self.declare(Fact(novel="在港综成为传说"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="yes"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="no"))
	def novel_11(self):
		self.declare(Fact(novel="诸界末日在线"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="yes"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="yes"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_12(self):
		self.declare(Fact(novel="诸天谍影"))
	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="yes"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="yes"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="yes"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_13(self):
		self.declare(Fact(novel="诸天尽头"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="yes"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="yes"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="yes"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_14(self):
		self.declare(Fact(novel="诸天万界神龙系统"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="yes"),Fact(kungfu="no"),Fact(bizarre="yes"),Fact(Metropolis="yes"),Fact(powerful="yes"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="yes"),Fact(Competitive="no"))
	def novel_14(self):
		self.declare(Fact(novel="诸天之从新做人"))

	@Rule(Fact(action='find_novel'),Fact(fantasy="no"),Fact(kungfu="no"),Fact(bizarre="no"),Fact(Metropolis="no"),Fact(powerful="no"),Fact(twoD="no"),Fact(Immortal="no"),Fact(sciencefiction="no"),Fact(onlinegames="no"),Fact(military="no"),Fact(history="no"),Fact(Supernatural="no"),Fact(Competitive="no"))
	def novel_15(self):
		self.declare(Fact(novel="别看小说了，你这也没适合的"))

	@Rule(Fact(action='find_novel'),Fact(novel=MATCH.novel),salience = -998)
	def novel(self, novel):
		print("")
		id_novel = novel
		novel_details = get_details(id_novel)
		treatments = get_treatments(id_novel)
		print("")
		print("The most probable novel that you have is %s\n" %(id_novel))
		print("A short description of the novel is given below :\n")
		print(novel_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

	@Rule(Fact(action='find_novel'),
		  Fact(fantasy=MATCH.fantasy),
		  Fact(kungfu=MATCH.kungfu),
		  Fact(bizarre=MATCH.bizarre),
		  Fact(Metropolis=MATCH.Metropolis),
		  Fact(powerful=MATCH.powerful),
		  Fact(twoD=MATCH.twoD),
		  Fact(Immortal=MATCH.Immortal),
		  Fact(onlinegames=MATCH.onlinegames),
		  Fact(sciencefiction=MATCH.sciencefiction),
		  Fact(military=MATCH.military),
		  Fact(history=MATCH.history),
		  Fact(Supernatural=MATCH.Supernatural),
		  Fact(Competitive=MATCH.Competitive),NOT(Fact(novel=MATCH.novel)),salience = -999)
	def not_matched(self,fantasy, kungfu, bizarre, Metropolis, powerful, twoD, Immortal, sciencefiction,onlinegames ,military ,history ,Supernatural ,Competitive):
		print("\n 系统无法判断你的想法，下面给出基于系统内最相近的推荐，如不满意请另请高人")
		lis = [fantasy, kungfu, bizarre, Metropolis, powerful, twoD, Immortal, sciencefiction,onlinegames ,military ,history ,Supernatural ,Competitive]
		max_count = 0
		max_novel = ""
		for key,val in feature_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_novel = val
		if_not_matched(max_novel)


if __name__ == "__main__":
	preprocess()
	engine = NovelF()
	engine.reset()  # Prepare the engine for the execution.
	engine.run()  # Run it!
	engine.matcher.show_network().view(filename="novel_intro_decisionTree",directory="./")

# import pandas as pd
# f = pd.DataFrame(novel_features)
# f.columns = ['玄幻','武侠','奇幻','都市','异能','仙侠','历史','网游','科幻','二次元','军事','灵异','竞技']
# n = pd.DataFrame(novel_list)
# f.insert(0,'小说名称',novel_list,allow_duplicates=False)