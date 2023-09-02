


def run() -> None:
  print("Suponiendo que el bioplastico total es el producido\n")
  
  yield_ha_to_bioplastic = 3.39 * 1000 * 0.057 * 0.87 # 1000 is the conversion factor kg/Tn
  bioplastic_calculated = yield_ha_to_bioplastic * 800000
  weight_plastic = 359000000 * 1000 # 1000 is the conversion factor kg/Tn
  bioplastic_present = 0.015 * weight_plastic
  print(int(bioplastic_calculated/1000), "Tn calculadas con rendimiento mínimo")
  print("proporción real/calculado=", int(bioplastic_present/bioplastic_calculated))

  bioplastic_estimated = 0.6 * weight_plastic # plastic per porcent bioplastic
  # calculate it using our conversion factor or yield but inverse
  ha_needed = bioplastic_estimated / yield_ha_to_bioplastic 
  print("se necesitan", ha_needed, "hectareas")
  ha_percent_total = ha_needed*100/((3.3+1.7)*1000000000)
  ha_percent_arable = ha_needed*100/(1.7*1000000000)
  print(round(ha_percent_total, 2), "% Global agricultaral area")
  print(round(ha_percent_arable, 2), "% Global arable area")

  print("\nSuponiendo que el bioplastico total es el producido en los 0.8M de hectareas\
  con el rendimiento mínimo usado para hacer los calculos de este programa\n")

  yield_ha_to_bioplastic = 3.39 * 1000 * 0.057 * 0.87 # 1000 is the conversion factor kg/Tn
  bioplastic_calculated = yield_ha_to_bioplastic * 800000
  weight_plastic = 359000000 * 1000 # 1000 is the conversion factor kg/Tn
  bioplastic_present = 0.015 * weight_plastic
  print(int(bioplastic_calculated/1000), "Tn calculadas con rendimiento mínimo")
  print("proporción real/calculado=", int(bioplastic_present/bioplastic_calculated))

  bioplastic_estimated = 40 * bioplastic_calculated
  ha_needed = bioplastic_estimated / yield_ha_to_bioplastic
  print("se necesitan", ha_needed, "hectareas")
  ha_percent_total = ha_needed*100/((3.3+1.7)*1000000000)
  ha_percent_arable = ha_needed*100/(1.7*1000000000)
  print(round(ha_percent_total, 2), "% Global agricultaral area")
  print(round(ha_percent_arable, 2), "% Global arable area")


if __name__ == "__main__":
  run()