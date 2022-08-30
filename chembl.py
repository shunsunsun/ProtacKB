
from chembl_webresource_client.new_client import new_client
from tqdm import tqdm
#from chembl_webresource_client.http_errors import HttpBadRequest, HttpApplicationError

def RetMech(chemblIds) -> dict:
    """Function to retrieve mechanism of actions and target proteins from ChEMBL

    :param chemblIds:
    :return:
    """
    getMech = new_client.mechanism

    mechList = []
    for chemblid in tqdm(chemblIds, desc='Retrieving mechanisms from ChEMBL'):
        mechs = getMech.filter(
            molecule_chembl_id=chemblid
        ).only(['mechanism_of_action', 'target_chembl_id'])
        mechList.append(list(mechs))

    named_mechList = dict(zip(chemblIds, mechList))
    named_mechList = {
        k: v
        for k, v in named_mechList.items()
        if v
    }
    return named_mechList

def RetDrugInd(chemblIDs) -> dict:
    """Function to retrieve associated diseases from ChEMBL

    :param chemblIDs:
    :return:
    """
    getDrugInd = new_client.drug_indication

    drugIndList = []
    for chemblid in tqdm(chemblIDs, desc='Retrieving diseases from ChEMBL'):
        drugInd = getDrugInd.filter(
            molecule_chembl_id=chemblid
        ).only('mesh_heading')
        drugIndList.append(list(drugInd))

    named_drugIndList = dict(zip(chemblIDs, drugIndList))
    named_drugIndList = {
        k: v
        for k, v in named_drugIndList.items()
        if v
    }
    return named_drugIndList