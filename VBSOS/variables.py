# variables

variables['detajj']  = {   'name': 'fabs(detajj)',
                           'range' : (20,3.5,9),
                           'xaxis' : '#Delta#eta_{jj}',
                           'fold' : 3
                        }
variables['ptll']    = {    'name': 'ptll',               
                            'range' : (20,30,200),   
                            'xaxis' : 'pt_{ll} [GeV]', 
                            'fold' : 3
                        }
variables['eta1']  = {   'name': 'Lepton_eta[0]',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3
                        }
variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold' : 3
                        }     
variables['detall']  = {   'name': 'fabs(Lepton_eta[0]-Lepton_eta[1])',
                           'range' : (20,0,6),
                           'xaxis' : '#Delta#eta_{ll}',
                           'fold'  : 3
                        }

variables['jetpt1']  = {   'name': 'Alt(CleanJet_pt,0,-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 1^{st} jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt(CleanJet_pt,1,-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 2^{nd} jet',
                           'fold'  : 3
                           }

variables['met']  = {   'name': 'MET_pt',            
                        'range' : (50,0,250),    
                        'xaxis' : 'MET [GeV]',
                        'fold'  : 3
                        }

variables['dphill']  = {'name': 'fabs(dphill)',
                        'range' : (20,0,3.5),
                        'xaxis' : '#Delta#Phi_{ll}',
                        'fold'  : 3
                        }

variables['dphijj']  = {'name': 'fabs(Alt(CleanJet_phi,0,-9999.)-Alt(CleanJet_phi,1,-9999.))',
                        'range' : (20,0,9),
                        'xaxis' : '#Delta#Phi_{jj}',
                        'fold'  : 3
                        }
variables['Mll']  = {       'name': 'mll',
                            'range' : (20,0,350),
                            'xaxis' : 'm_{ll} [GeV]',
                            'fold'  : 3
                        }
variables['btag_central']  = {   'name'  : '(fabs(Alt(CleanJet_eta,0,-9999.)) <= fabs(Alt(CleanJet_eta,1,-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt(CleanJet_eta,1,-9999.)) < fabs(Alt(CleanJet_eta,0,-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]]',
                                'range' : (20,0,1),
                                'xaxis' : 'b-tag of the 1^{st} most central jet',
                                'fold'  : 3
                            }
variables['dR_jl1'] = {	'name' : '(R_j1l1 < R_j2l1)*R_j1l1+(R_j1l1 >= R_j2l1)*R_j2l1',
                        'range' : (50,0,10),
                        'xaxis' : 'R from 1^{st} lep to nearest jet',
                        'fold'  : 3
                            }
variables['dR_jl2'] = { 'name' : '(R_j1l2 < R_j2l2)*R_j1l2+(R_j1l2 >= R_j2l2)*R_j2l2',
                        'range' : (50,0,10),
                        'xaxis' : 'R from 2^{nd} lep to nearest jet',
                        'fold'  : 3
                            }
variables['Zeppll']  = {   'name': 'Zeppll_al',
                           'range' : (10,0,1),
                           'xaxis' : 'Zeppenfeld_{ll}',
                           'fold' : 3
                           }  
variables['Zepp1']  = {   'name': 'Zepp1_al',
                           'range' : (10,-5,5),
                           'xaxis' : 'Zeppenfeld_{1}',
                           'fold' :0
                           }
variables['Zepp2']  = {   'name': 'Zepp2_al',
                           'range' : (10,-5,5),
                           'xaxis' : 'Zeppenfeld_{2}',
                           'fold' :0
                           }
variables['mjj']  = {   'name': 'mjj',
                        'range' : (10,400,3000),
                        'xaxis' : 'm_{jj} [GeV]',
                        'fold' : 3
                        } 

variables['events']  = {'name': '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                        'fold' : 3
                        }

variables['qgl_forward'] = { 'name': 'qgl_forward',
                         'range' : (50, 0, 1),
                         'xaxis' : 'Quark vs Gluon likelihood discriminator - Forward jet',
                         'fold' : 3
                       }
                       
variables['qgl_central'] = { 'name': 'qgl_central',
                         'range' : (50, 0, 1),
                         'xaxis' : 'Quark vs Gluon likelihood discriminator - Central jet',
                         'fold' : 3
                       }
                       

# variables['Jet_mult'] = { 'name': 'Jet_nConstituents',
#                          'range' : (15, 0, 150),
#                          'xaxis' : 'Number of particles in the jet',
#                          'fold' : 3
#                        }