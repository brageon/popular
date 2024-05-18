import csv
import pandas as pd
with open('../Action.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Act.csv', mode='a')
with open('../Action.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Act.csv', mode='a')
with open('../Adventure.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Adv.csv', mode='a')
with open('../Adventure.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Adv.csv', mode='a')
with open('../Arcade.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Arc.csv', mode='a')
with open('../Arcade.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Arc.csv', mode='a')
with open('../Beauty.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bet.csv', mode='a')
with open('../Beauty.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bet.csv', mode='a')
with open('../Board.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bod.csv', mode='a')
with open('../Board.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bod.csv', mode='a')
with open('../Books.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bok.csv', mode='a')
with open('../Books.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bok.csv', mode='a')
with open('../Business.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bus.csv', mode='a')
with open('../Business.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Bus.csv', mode='a')
with open('../Card.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Car.csv', mode='a')
with open('../Card.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Car.csv', mode='a')
with open('../Casual.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Cas.csv', mode='a')
with open('../Casual.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Cas.csv', mode='a')
with open('../Casino.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Ino.csv', mode='a')
with open('../Casino.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Ino.csv', mode='a')
with open('../Comics.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Com.csv', mode='a')
with open('../Comics.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Com.csv', mode='a')
with open('../Communication.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Cop.csv', mode='a')
with open('../Communication.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Cop.csv', mode='a')
with open('../Dating.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Dat.csv', mode='a')
with open('../Dating.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Dat.csv', mode='a')
with open('../Design.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Des.csv', mode='a')
with open('../Design.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Des.csv', mode='a')
with open('../Education.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Edu.csv', mode='a')
with open('../Education.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Edu.csv', mode='a')
with open('../Entertainment.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Ent.csv', mode='a')
with open('../Entertainment.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Ent.csv', mode='a')
with open('../Events.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Eve.csv', mode='a')
with open('../Events.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Eve.csv', mode='a')
with open('../Finance.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Fin.csv', mode='a')
with open('../Finance.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Fin.csv', mode='a')
with open('../Food.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Foo.csv', mode='a')
with open('../Food.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Foo.csv', mode='a')
with open('../House.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Hem.csv', mode='a')
with open('../House.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Hem.csv', mode='a')
with open('../Libraries.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Lib.csv', mode='a')
with open('../Libraries.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Lib.csv', mode='a')
with open('../Lifestyle.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Lif.csv', mode='a')
with open('../Lifestyle.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Lif.csv', mode='a')
with open('../Maps.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Map.csv', mode='a')
with open('../Maps.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Map.csv', mode='a')
with open('../Medical.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Med.csv', mode='a')
with open('../Medical.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Med.csv', mode='a')
with open('../Music.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Mus.csv', mode='a')
with open('../Music.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Mus.csv', mode='a')
with open('../News.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('New.csv', mode='a')
with open('../News.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('New.csv', mode='a')
with open('../Parenting.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Par.csv', mode='a')
with open('../Parenting.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Par.csv', mode='a')
with open('../Photography.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Pho.csv', mode='a')
with open('../Photography.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Pho.csv', mode='a')
with open('../Productivity.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Pro.csv', mode='a')
with open('../Productivity.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Pro.csv', mode='a')
with open('../Puzzle.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Puz.csv', mode='a')
with open('../Puzzle.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Puz.csv', mode='a')
with open('../Racing.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Rac.csv', mode='a')
with open('../Racing.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Rac.csv', mode='a')
with open('../Role.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Rol.csv', mode='a')
with open('../Role.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Rol.csv', mode='a')
with open('../Shopping.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Sho.csv', mode='a')
with open('../Shopping.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Sho.csv', mode='a')
with open('../Simulation.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Sim.csv', mode='a')
with open('../Simulation.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Sim.csv', mode='a')
with open('../Social.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Soc.csv', mode='a')
with open('../Social.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Soc.csv', mode='a')
with open('../Sports.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Spo.csv', mode='a')
with open('../Sports.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Spo.csv', mode='a')
with open('../Strategy.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Sta.csv', mode='a')
with open('../Strategy.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Sta.csv', mode='a')
with open('../Tools.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Tol.csv', mode='a')
with open('../Tools.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Tol.csv', mode='a')
with open('../Travel.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Tra.csv', mode='a')
with open('../Travel.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Tra.csv', mode='a')
with open('../Trivia.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Triv.csv', mode='a')
with open('../Trivia.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Triv.csv', mode='a')
with open('../Vehicles.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Veh.csv', mode='a')
with open('../Vehicles.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Veh.csv', mode='a')
with open('../Video.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Vid.csv', mode='a')
with open('../Video.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Vid.csv', mode='a')
with open('../Weather.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Wea.csv', mode='a')
with open('../Weather.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Wea.csv', mode='a')
with open('../Word.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['rating_five_star'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Woo.csv', mode='a')
with open('../Word.csv', 'r') as file:
    reader = csv.DictReader(file)
    highest = sorted(reader, key=lambda x: 
    x['reviews'])[-10:]
df = pd.DataFrame(highest)
df.to_csv('Woo.csv', mode='a')