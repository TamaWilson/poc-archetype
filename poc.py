import os 

appName = input("Qual nome da Aplicação? (Sem Espaço) ")
groupId = input("Digite o Groupid: ")
artifactId = input("Digite o ArtifactId: ")
lombok = "true" if input("Incluir Lombok? (S/N) ").lower() == "s" else "false"
postgres = "true" if input("Incluir Postgres? (S/N) ").lower() == "s" else "false"

installComannd = "mvn clean install"
createCommand = f"""mvn archetype:generate "-DoutputDirectory=../" "-DinteractiveMode=false" "-DarchetypeGroupId=br.com.tamawilson" "-DarchetypeArtifactId=poc-archetype" "-DarchetypeVersion=1.0-SNAPSHOT" "-DgroupId={groupId}" "-DartifactId={artifactId}" "-Dlombok={lombok}" "-Dpostgres={postgres}" "-DappName={appName}"""

print(createCommand)
os.system(f"{createCommand}")
