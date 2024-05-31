
fruit={
    'pomme':'rouge',
    'banane':'jaune',
    'orange':'orange'
}

fruit['kiwi']='vert'

couleur_banane=fruit['banane']

fruit['pomme']='vert'

del fruit['orange']

print(fruit.values())