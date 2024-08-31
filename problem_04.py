def calculate_share(share, Total):
    return round(share/Total * 100);

estados_fat = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
estado_select = input('Digite o estado (SP, RJ, MG, ES ou Outros):')
total_faturamento = sum(estados_fat.values())
estado_share = calculate_share(estados_fat[estado_select], total_faturamento)
print(f"O percentual do estado {estado_select} é {estado_share}%")
