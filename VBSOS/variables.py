# variables

#variables = {}

#
variables['detajj']  = {   'name': 'AbsVec(detajj)',
                           'range' : (20,0,9),
                           'xaxis' : '#Delta#eta_{jj}',
                           'fold' : 3
                        }
variables['detall']  = {   'name': 'AbsVec(Alt(Lepton_eta,0,-9999.)-Alt(Lepton_eta,1,-9999.))',
                           'range' : (20,0,6),
                           'xaxis' : '#Delta#eta_{ll}',
                           'fold'  : 3
                        }
variables['eta1']  = {   'name': 'Alt(Lepton_eta,0,-9999.)',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3
                        }
variables['eta2']  = {  'name': 'Alt(Lepton_eta,1,-9999.)',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold' : 3
                        }                         
variables['jetpt1']  = {   'name': 'Alt(CleanJet_pt,0,-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold' : 3
                           }

variables['jetpt2']  = {   'name': 'Alt(CleanJet_pt,1,-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold' : 3
                           }
variables['dphill']  = {'name': 'AbsVec(dphill)',
                        'range' : (20,0,3.5),
                        'xaxis' : '#Delta#Phi_{ll}',
                        'fold'  : 3
                        }

variables['dphijj']  = {'name': 'AbsVec(Alt(CleanJet_phi,0,-9999.)-Alt(CleanJet_phi,1,-9999.))',
                        'range' : (20,0,9),
                        'xaxis' : '#Delta#Phi_{jj}',
                        'fold'  : 3
                        }
variables['met']  = {   'name': 'MET_pt',            #   variable name
                        'range' : (50,0,250),    #   variable range
                        'xaxis' : 'MET [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['Zlep1']  = {  'name': '(Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj',
                         'range': (20,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{1}',
                         'fold'  : 3
                         }
variables['Zlep2']  = {  'name': '(Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj',
                         'range': (200,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{2}',
                         'fold'  : 3
                        }
variables['Mll']  = {       'name': 'mll',
                            'range' : (20,0,350),
                            'xaxis' : 'm_{ll} [GeV]',
                            'fold'  : 3
                        }
variables['btag_first']  = {   'name'  : '(AbsVec(CleanJet_eta[0]) <= AbsVec(CleanJet_eta[1])) * Take(Jet_btagDeepB,CleanJet_jetIdx[0]) + (AbsVec(CleanJet_eta[0]) > AbsVec(CleanJet_eta[1])) * Take(Jet_btagDeepB,CleanJet_jetIdx[1])',
                              'range' : (20,0,1),
                              'xaxis' : 'b-tag of 1^{st} most central jet',
                             'fold'  : 3
                       }

variables['btag_second']  = {   'name'  : '(AbsVec(CleanJet_eta[0]) > AbsVec(CleanJet_eta[1])) * Take(Jet_btagDeepB,CleanJet_jetIdx[0]) + (AbsVec(CleanJet_eta[0]) <= AbsVec(CleanJet_eta[1])) * Take(Jet_btagDeepB,CleanJet_jetIdx[1])',
                              'range' : (20,0,1),
                              'xaxis' : 'b-tag of 2^{nd} most central jet',
                             'fold'  : 3
                       }

variables['dR_jl1'] = { 'name' : '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1',
 				'range' : (20,0,4),
                                'xaxis' : 'R from 1^{st} lep to nearest jet',
                              'fold'  : 3
                         }

variables['dR_jl2'] = { 'name' : '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2',
                                'range' : (20,0,4),
                                'xaxis' : 'R from 2^{nd} lep to nearest jet',
                                'fold'  : 3
                            }

