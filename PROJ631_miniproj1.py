##PROJ631 Mini-projet 1 : Stockage de données personnelles en Python

from collections import Counter
import copy

class Data :

    def __init__(self, id, size) :
        self.id = id
        self.size = size


class User :

    def __init__(self, id, L_data_ID, node_ID) :
        self.id = id
        self.userdata = L_data_ID
        self.usernodeID = node_ID


class SysNode :

    def __init__(self, id, memsize, L_stocked_data, L_reachable_nodes, L_times) :
        self.id = id
        self.memsize = memsize
        self.localdata = L_stocked_data
        self.reachablenodes = L_reachable_nodes
        self.times = L_times            #Cette liste contient les poids pour aller au noeud qui se trouve au même indice dans la liste reachablenodes

    def timeto(self, id) :
        for i in range(len(self.reachablenodes)) :
            if self.reachablenodes[i] == id :
                return(self.times[i])
        return("Ce noeud n'est pas atteignable.")

    def availableMemSize(self) :
        s = 0
        for i in self.localdata :
            s = s + i.size
        return(self.memsize - s)

    def addData(self, data) :
        if self.availableMemSize() >= data.size :
            self.localdata.append(data)
            print('Confirm Added')
        else :
            return('ERREUR : pas assez de place dans la donnée')



'''class Arcs :

    def __init__(self, id, time) :
        self.id = id
        self.time = time'''


class System :

    def __init__(self, L_nodes, L_users, L_data) :
        self.nodes = L_nodes
        self.users = L_users
        self.data = L_data


    '''def placedata(self, user) :
        if not user in self.users :             #check d'utilisateur valide
            return("Cet utilisateur ne fait pas partie du système.")
        for n in self.nodes :
            if n.id == user.usernodeID :            #récupération du node lié à l'utilisateur
                usernode = n
        nodesreft, times = self.alltimesfrom(usernode)
        for d in user.userdata :
            result = self.subplacedata(d, nodesreft, times)
            if type(result) == str :
                return(result)
        return('Terminé.')'''

    '''else :
            for n in self.nodes :
                if n.id == user.usernodeID :
                    usernode = n
            for n in self.nodes :               #check de données déjà placées
                for d in user.userdata :
                    for l in n.localdata :
                        #print('checkdata', d, n.localdata)
                        if d.id == l.id :
                            return("Les données sont déjà placées.")
            dataToPlace = copy.deepcopy(user.userdata)
            nodesreft, times = self.alltimesfrom(usernode)
            #times.append(0)
            #nodesreft.append(usernode)
            timesReset = copy.deepcopy(times)               #sauvegarde des listes entières
            nodesreftReset = copy.deepcopy(nodesreft)
            while times != [] and dataToPlace != [] :           #tant qu'il reste des noeuds à vérifier ou des données à placer
                print(times, dataToPlace)
                for i in range(len(times)) :
                    if times[i] == min(times) :
                        minInd = i              #indice du noeud à vérifier
                times.pop(minInd)
                currentnode = nodesreft.pop(minInd)
                if currentnode.availableMemSize() >= dataToPlace[0].size :
                    print('va placer, ', currentnode.localdata)
                    dataPlaced = dataToPlace.pop(0)
                    currentnode.addData(dataPlaced)
                    print('placé', dataPlaced, currentnode.id, currentnode.localdata)
                    times = copy.deepcopy(timesReset)               #réinitialisation des parcours pour chaque nouvelle donnée
                    nodesreft = copy.deepcopy(nodesreftReset)
            if times == [] and dataToPlace != [] :
                return('Pas assez de place.')
            else :
                return('Terminé.')'''

    '''def subplacedata(self, Edata, nodesreft, times) :
        for n in self.nodes :
            for l in n.localdata :          #check de données déjà placées
                if Edata.id == l.id :
                    return("Les données sont déjà placées.")
            while times != [] :           #tant qu'il reste des noeuds à vérifier
                print(times)
                for i in range(len(times)) :
                    if times[i] == min(times) :
                        minInd = i              #indice du noeud à vérifier
                times.pop(minInd)
                currentnode = nodesreft.pop(minInd)
                if currentnode.availableMemSize() >= Edata.size :
                    print('va placer, ', currentnode.localdata)
                    currentnode.addData(Edata)
                    print('placé', Edata.id, currentnode.id, currentnode.localdata)
                    return(True)
            if times == [] :
                return('Pas assez de place.')       #communique "Pas assez de place".'''


    def placedataworksonce(self, user) :
        print('placedataworksonce called')
        #if not user in self.users :             #check d'utilisateur valide
            #return("Cet utilisateur ne fait pas partie du système.")
        #else :
        for n in self.nodes :
            if n.id == user.usernodeID :
                usernode = n
        '''for n in self.nodes :               #check de données déjà placées
            for d in user.userdata :
                for l in n.localdata :
                    #print('checkdata', d, n.localdata)
                    if d.id == l.id :
                        return("Les données sont déjà placées.")'''
        dataToPlace = copy.deepcopy(user.userdata)
        nodesreft, times = self.alltimesfrom(usernode)
        times.append(0)
        nodesreft.append(usernode)
        timesReset = copy.deepcopy(times)               #sauvegarde des listes entières
        nodesreftReset = copy.deepcopy(nodesreft)
        while times != [] and dataToPlace != [] :           #tant qu'il reste des noeuds à vérifier ou des données à placer
            print(times, dataToPlace)
            for i in range(len(times)) :
                if times[i] == min(times) :
                    minInd = i              #indice du noeud à vérifier
            times.pop(minInd)
            currentnode = nodesreft.pop(minInd)
            if currentnode.availableMemSize() >= dataToPlace[0].size :
                print('va placer, ', currentnode.localdata)
                dataPlaced = dataToPlace.pop(0)
                currentnode.addData(dataPlaced)
                print('placé', dataPlaced, currentnode.id, currentnode.localdata)
                times = copy.deepcopy(timesReset)               #réinitialisation des parcours pour chaque nouvelle donnée
                nodesreft = copy.deepcopy(nodesreftReset)
        '''if times == [] and dataToPlace != [] :
            return('Pas assez de place.')
        else :
            return('Terminé.')'''

    def placedatascotch(self, user) :
        if not user in self.users :             #check d'utilisateur valide
            return("L''utilisateur ne fait pas partie du système.")
        else :
            for n in self.nodes :               #check de données déjà placées
                for d in user.userdata :
                    for l in n.localdata :
                        #print('checkdata', d, n.localdata)
                        if d.id == l.id :
                            return("Les données sont déjà placées.")
            for n in self.nodes :
                if n.id == user.usernodeID :            #récupération du node lié à l'utilisateur
                    usernode = n
            nodesreft, times = self.alltimesfrom(usernode)
            timesReset = copy.deepcopy(times)               #sauvegarde des listes entières
            nodesreftReset = copy.deepcopy(nodesreft)
            for d in user.userdata :
                times = copy.deepcopy(timesReset)               #réinitialisation des parcours pour chaque nouvelle donnée
                nodesreft = copy.deepcopy(nodesreftReset)
                while times !=[] :
                    for i in range(len(times)) :
                        if times[i] == min(times) :
                            minInd = i
                    times.pop(minInd)
                    currentnode = nodesreft.pop(minInd)
                    if currentnode.availableMemSize() >= d.size :
                        scotchuser = User(100, [d], currentnode.id)
                        #self.addUser(scotchuser)
                        self.placedataworksonce(scotchuser)
                        #self.removeUser(scotchuser)
                        times = []                      #fin boucle while
                        print('placé', d.id, currentnode.id)
        return('Terminé fr.')


    def placedataQ3(self, user1, user2) :
        if not user1 in self.users :             #check d'utilisateurs valides
            return("L'utilisateur 1 ne fait pas partie du système.")
        if not user2 in self.users :             #check d'utilisateur valide
            return("L'utilisateur 2 ne fait pas partie du système.")
        dataToPlace = []
        for i in user1.userdata :
            for j in user2.userdata :
                if i.id == j.id :
                    dataToPlace.append(i)           #récupération des données en commun
        for n in self.nodes :
            if n.id == user1.usernodeID :            #récupération du node lié à l'utilisateur
                usernode1 = n
            if n.id == user2.usernodeID :
                usernode2 = n
        nodesreft, times1 = self.alltimesfrom(usernode1)
        nodesreft2temp, times2temp = self.alltimesfrom(usernode2)
        times2 = []
        for i in nodesreft :    #organiser les 2 listes pour qu'elles réfèrent aux mêmes noeuds
            for j in range(len(nodesreft2temp)) :
                if i.id == nodesreft2temp[j].id :
                    times2.append(times2temp[j])
        #print(times1, times2)
        AVGtimes = []
        difftimes = []
        for i in range(len(times1)) :
            AVGtimes.append((times1[i] + times2[i])/2)      #calcul des temps moyens
            difftimes.append(abs(times1[i] - times2[i]))    #calcul des différences absolues
        #print(AVGtimes, difftimes)
        # #===========AFFICHAGE DEBUG DES NOEUDS===============
        # nodeids = []
        # for i in nodesreft :
        #     nodeids.append(i.id)
        # print(nodeids)
        # #====================================================
        while AVGtimes != [] :          #boucle principale
            AVGmin = min(AVGtimes)
            AVGminInd = []
            #print('AVGmin', AVGmin)
            for i in range(len(AVGtimes)) :     #récupération des IDs des temps minimums
                if AVGtimes[i] == AVGmin :
                    AVGminInd.append(i)
            #print('index', AVGminInd)
            currentnodes = []
            currentdiffs = []
            for i in range(len(AVGminInd) - 1, -1, -1) :
                #print(AVGminInd[i], nodesreft[i])
                AVGtimes.pop(AVGminInd[i])          #suppression des temps minimums
                currentnodes.append(nodesreft[AVGminInd[i]])       #récupération des noeuds en traitement
                currentdiffs.append(difftimes[AVGminInd[i]])       #récupération des différences concernées
                difftimes.pop(i)
            # #===========AFFICHAGE DEBUG DES NOEUDS===============
            # nodeids = []
            # for i in currentnodes :
            #     nodeids.append(i.id)
            # print(nodeids)
            # #====================================================
            while currentdiffs != [] and dataToPlace != [] :
                for i in range(len(currentdiffs)) :
                    if currentdiffs[i] == min(currentdiffs) :
                        placeInd = i
                currentdiffs.pop(placeInd)
                #print(currentnodes[placeInd].id)
                if currentnodes[placeInd].availableMemSize() > dataToPlace[0].size :
                    dataPlaced = dataToPlace.pop(0)
                    scotchuser = User(100, [dataPlaced], currentnodes[placeInd].id)
                    self.placedataworksonce(scotchuser)
                currentnodes.pop(placeInd)


    def placedataQ4(user) :
        pass

    def addUser(self, user) :
        self.users.append(user)

    def removeUser(self, user) :
        self.users.remove(user)


    def cleardata(self) :
        print("Êtes-vous sûr de vouloir effacer les données du système ? Cela ne supprimera que les données présentes localement dans les noeuds système, vous pourrez toujours les replacer à partir des données utilisateurs. Tapez 'oui' pour continuer.")
        if input() == 'oui' :
            for i in range(len(self.nodes)) :
                self.nodes[i].localdata = []
            return("Terminé.")
        else :
            return("Annulé.")


    def alltimesfrom(self, node) :
        allnodes = copy.deepcopy(self.nodes)
        alltimes = [0 for i in range(len(allnodes))]
        for i in range(len(node.reachablenodes)) :
            for j in range(len(allnodes)) :
                if node.reachablenodes[i] == allnodes[j].id :
                    alltimes[j] = node.times[i]     #ajout des temps de tous les noeuds atteignables de base
        #currentnode = node
        #timefromstart = 0
        process = True
        #choosenewnode = True
        for sysnode in allnodes :
            currentnode = sysnode
            for i in range(len(allnodes)) :                #recherche du timefromstart
                if currentnode.id == allnodes[i].id :
                    timefromstart = alltimes[i]
            nodestovisitID = []
            visitednodesID = [node.id]
            choosenewnode = False
            for n in allnodes :
                if n.id != node.id :
                    nodestovisitID.append(n.id)
            while len(nodestovisitID) > 1 :
                if choosenewnode :
                    accessiblenodesID = currentnode.reachablenodes[:]
                    accessiblenodestimes = currentnode.times[:]
                    #print('CURRENTSTATE', currentnode.id, visitednodesID, nodestovisitID)
                    #print('accnodebefore', accessiblenodesID)
                    usernodesind = []
                    for i in range(len(accessiblenodesID)) :
                        if accessiblenodesID[i] >= 100 :        #recherche de noeuds utilisateurs
                            usernodesind.append(i)
                    usernodesind.reverse()
                    for ind in usernodesind :               #suppression des noeuds utilisateurs
                        accessiblenodesID.pop(ind)
                        accessiblenodestimes.pop(ind)
                    for v in visitednodesID :
                        #print('----- entering danger zone -----')
                        #print(v, accessiblenodesID, v in accessiblenodesID)
                        if v in accessiblenodesID :
                            looking = True
                            i = 0
                            length = len(accessiblenodesID)
                            while i < length :
                                #print(looking, visitednodesID)
                                if looking and v == accessiblenodesID[i] :
                                    #print(v, nodestovisitID, accessiblenodesID, i)
                                    accessiblenodesID.pop(i)            #suppression des noeuds déjà visités
                                    accessiblenodestimes.pop(i)
                                    i = i - 1
                                    length = length - 1
                                    looking = False
                                i = i + 1
                    #print ('===== fin danger zone =====')
                    #print('accnode      ', accessiblenodesID)
                    if accessiblenodesID != [] :
                        m = min(accessiblenodestimes)
                        for i in range(len(accessiblenodestimes)) :
                            if accessiblenodestimes[i] == m :
                                newnodeID = accessiblenodesID[i]       #recherche du prochain noeud à visiter
                                timefromstart = timefromstart + m
                                #print('newnodeID', newnodeID, timefromstart)
                                #print('times', alltimes)
                                break
                        for n in allnodes :
                            if n.id == newnodeID :
                                #print(currentnode.id, visitednodesID, nodestovisitID)
                                if currentnode.id != node.id :
                                    visitednodesID.append(currentnode.id)
                                    nodestovisitID.remove(currentnode.id)
                                currentnode = n                         #assignation du nouveau noeud
                choosenewnode = True    #assure que la boucle fonctionnera bien à nouveau
                for i in range(len(currentnode.reachablenodes)) :
                    for j in range(len(allnodes)) :
                        if currentnode.reachablenodes[i] == allnodes[j].id and (alltimes[j] == 0 or alltimes[j] >  timefromstart + currentnode.times[i]) :
                            #print(timefromstart, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                            alltimes[j] = timefromstart + currentnode.times[i]      #ajout du temps mesuré
                            #print('CHANGEMENT : NOUVEAU TEMPS')
                #print('Fin boucle donnée')
            '''for i in range(len(allnodes)) :
                for j in range(len(node.reachablenodes)) :
                    print(allnodes[i].id, node.reachablenodes[j], ' | ', alltimes[i], node.times[j])
                    if allnodes[i].id == node.reachablenodes[j] and alltimes[i] > node.times[j] :   #vérification qu'il n'y a pas de temps absurde
                        currentnode = allnodes[i]
                        timefromstart = node.times[j]
                        choosenewnode = False   #permet de passer la partie d'assignation dans le prochain passage de la boucle while
                        print('fin main boucle AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                    else : process = False'''      #si aucune erreur n'est détectée, la boucle s'arrête.
            #print('Fin boucle principale AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        for i in range(len(allnodes)) :          #suppression du noeud en entrée
            #print(allnodes[i].id, node.id)
            if allnodes[i].id == node.id :
                node_ind = i
        #allnodes.pop(node_ind)
        alltimes[node_ind] = 0
        return(allnodes, alltimes)
#CA MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARCHE OUIIIIIIIIIIIIIIIII



    def displaystate(self) :
        for i in self.nodes :
            dataids = []
            for d in i.localdata :
                dataids.append(d.id)
            print('Node with id ' + str(i.id) + ' stores data with the following ids : ', dataids)


    def alltimesfromhumantest(self, node) :
        nodes, times = self.alltimesfrom(node)
        for i in range(len(nodes)) :
            nodes[i] = nodes[i].id
        return(nodes, times)




#Exemple d'une structure de données (énoncé Figure 1)
#je choisis de dire que 1000<DATA_id<10000, 10<USER_id<100, 100<NODE_id<1000
Data0 = Data(1000, 25)
Data1 = Data(1001, 25)
Data2 = Data(1002, 30)
Data3 = Data(1003, 20)
Data4 = Data(1004, 40)
Data5 = Data(1005, 20)
Data6 = Data(1006, 20)
Data7 = Data(1007, 20)
Data8 = Data(1008, 50)
Data9 = Data(1009, 10)
DataC1 = Data(1010, 25)
DataC2 = Data(1011, 20)

User0 = User(100, [Data0], 10)
User1 = User(101, [Data1, Data2], 10)
User2 = User(102, [Data3, Data5], 10)
User3 = User(103, [Data4], 11)
User4 = User(104, [Data6, Data9], 12)
User5 = User(105, [Data8], 13)
User6 = User(106, [Data7], 13)
UserC1 = User(107, [DataC1], 10)
UserC2 = User(108, [DataC1, DataC2], 13)
UserC3 = User(109, [Data9, DataC1], 14)
UserC4 = User(110, [DataC1, DataC2], 10)

Node0 = SysNode(10, 50, [], [11, 12, 13, 14, 100, 101, 102], [1, 3, 3, 1, 2, 2, 2])
Node1 = SysNode(11, 40, [], [10, 12, 13, 14, 103], [1, 1, 3, 3, 2])
Node2 = SysNode(12, 50, [], [10, 11, 13, 14, 104], [3, 1, 1, 3, 2])
Node3 = SysNode(13, 40, [], [10, 11, 12, 14, 105, 106], [3, 3, 1, 1, 2, 2])
Node4 = SysNode(14, 40, [], [10, 11, 12, 13], [1, 3, 3, 1])

SysEnonce = System([Node0, Node1, Node2, Node3, Node4], [User0, User1, User2, User3, User4, User5, User6, UserC1, UserC2, UserC3, UserC4], [Data0, Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8, Data9, DataC1, DataC2])