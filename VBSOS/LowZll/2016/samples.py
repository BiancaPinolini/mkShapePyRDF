import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017_v6
configurations = os.path.dirname(configurations) # ggH 
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, getBaseWnAOD, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()
    
################################################
################# SKIMS ########################
################################################

mcProduction = 'Summer16_102X_nAODv5_Full2016v6'
mcSteps = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6{var}'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################
# ## TRAINING SAMPLES
# ###### Top #######
# files = nanoGetSampleFiles(mcDirectory, 'TTJets_DiLept') + \
#     nanoGetSampleFiles(mcDirectory, 'TTJets_DiLept_ext1')

# samples['top'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1,
# }

# addSampleWeight(samples,'top','TTJets_DiLept','Top_pTrw')

# ###########################################
# #############   SIGNALS  ##################
# ###########################################

# signals = []

# samples['WWewk'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
#     'weight': mcCommonWeight + '*(Sum(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*(lhe_mW1 > 63. && lhe_mW1 < 100. && lhe_mW2 > 63. && lhe_mW2 < 100.)', #filter tops and Higgs, limit w mass
#     'FilesPerJob': 4
# }


# signals.append('WWewk')


## TEST SAMPLES
###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')

signals = []
samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
    'weight': mcCommonWeight + '*(Sum(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*(lhe_mW1 > 63. && lhe_mW1 < 100. && lhe_mW2 > 63. && lhe_mW2 < 100.)', #filter tops and Higgs, limit w mass
    'FilesPerJob': 4
}

signals.append('WWewk')