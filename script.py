#
#  Copyright (C) 2002-2020 CERN for the benefit of the ATLAS collaboration
#

'''
@file InDetMonitoringGlobalRun3Test.py
@brief Top configuration of InDetMonitoringGlobalRun3Test in Run 3 style but in Run 2 environment
'''

import AthenaCommon.AtlasUnixStandardJob

from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()


from TrkTrackCollectionMerger.TrkTrackCollectionMergerConf import Trk__TrackCollectionMerger
LRTMerger = Trk__TrackCollectionMerger("LRTMerger",
TracksLocation        = [ "CombinedInDetTracks","ExtendedLargeD0Tracks"], 
OutputTracksLocation  = "StandardAndLRTTracks",
CreateViewColllection = True,
SummaryTool           = '',
AssociationTool       = '',
UpdateSharedHits      = False,
UpdateAdditionalInfo  = False)

topSequence += LRTMerger


doInDetGlobalTrackMonAlg           = True
doInDetGlobalPrimaryVertexMonAlg   = True
doInDetGlobalBeamSpotMonAlg        = True


from InDetGlobalMonitoringRun3Test.InDetGlobalMonitoringRun3TestConf import InDetGlobalTrackMonAlg
from InDetGlobalMonitoringRun3Test.InDetGlobalTrackMonAlgCfg import InDetGlobalTrackMonAlgCfg

from InDetGlobalMonitoringRun3Test.InDetGlobalMonitoringRun3TestConf import InDetGlobalPrimaryVertexMonAlg
from InDetGlobalMonitoringRun3Test.InDetGlobalPrimaryVertexMonAlgCfg import InDetGlobalPrimaryVertexMonAlgCfg

from InDetGlobalMonitoringRun3Test.InDetGlobalMonitoringRun3TestConf import InDetGlobalBeamSpotMonAlg
from InDetGlobalMonitoringRun3Test.InDetGlobalBeamSpotMonAlgCfg import InDetGlobalBeamSpotMonAlgCfg

from InDetRecExample.InDetKeys import InDetKeys
from AthenaMonitoring.DQMonFlags import DQMonFlags

kwargsInDetGlobalTrackMonAlg = {
    'DoIBL'      : True,                   #InDetFlags.doIBL(), #Turn on/off IBL histograms
    'TrackName'  : 'CombinedInDetTracks',  #InDetKeys.Tracks()
    'TrackName2' : 'CombinedInDetTracks',  #
    'TrackName3' : 'CombinedInDetTracks',  #
}

kwargsInDetGlobalPrimaryVertexMonAlg = { 
    'vxContainerName'                      : 'PrimaryVertices', #InDetKeys.xAODVertexContainer(),
    'vxContainerNameWithOutBeamConstraint' : 'VxPrimaryCandidateWithBeamConstraint', #InDetKeys.PrimaryVerticesWithoutBeamConstraint(),
    'vxContainerNameSplit'                 : 'VxPrimaryCandidateSplitStream', #InDetKeys.PrimaryVerticesSplitStream(),
    'doEnhancedMonitoring'                 : False # InDetFlags.doMonitoringPrimaryVertexingEnhanced()
}

kwargsInDetGlobalBeamSpotMonAlg = {
    'BeamSpotKey'                      : 'BeamSpotData', #InDetKeys.BeamSpotData(),
    'vxContainerName'                  : 'PrimaryVertices', #InDetKeys.xAODVertexContainer(),
    'trackContainerName'               : 'InDetTrackParticles', #InDetKeys.xAODTrackParticleContainer(),
    'useBeamspot'                      : True, # InDetFlags.useBeamConstraint()
    'vxContainerWithBeamConstraint'    : False # InDetFlags.useBeamConstraint()
}


# old magic
from AthenaMonitoring import AthMonitorCfgHelper
helper = AthMonitorCfgHelper(DQMonFlags, "InDetGlobalMonitoringRun3Test")


if doInDetGlobalTrackMonAlg:
  inDetGlobalTrackMonAlg = helper.addAlgorithm(InDetGlobalTrackMonAlg, 'InDetGlobalTrackMonAlg')
  for k, v in kwargsInDetGlobalTrackMonAlg.items():
      setattr(inDetGlobalTrackMonAlg, k, v)

  inDetGlobalTrackMonAlg.TrackSelectionTool.UseTrkTrackTools = True
  inDetGlobalTrackMonAlg.TrackSelectionTool.CutLevel         = "TightPrimary"
  inDetGlobalTrackMonAlg.TrackSelectionTool.maxNPixelHoles   = 1
  inDetGlobalTrackMonAlg.TrackSelectionTool.minPt            = 5000
  inDetGlobalTrackMonAlg.TrackSelectionTool.TrackSummaryTool = InDetTrackSummaryTool
  inDetGlobalTrackMonAlg.TrackSelectionTool.Extrapolator     = InDetExtrapolator

  inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.UseTrkTrackTools = True
  inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.CutLevel         = "TightPrimary"
  inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.minPt            = 5000
  inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.TrackSummaryTool = InDetTrackSummaryTool
  inDetGlobalTrackMonAlg.Tight_TrackSelectionTool.Extrapolator     = InDetExtrapolator

  InDetGlobalTrackMonAlgCfg(helper, inDetGlobalTrackMonAlg, **kwargsInDetGlobalTrackMonAlg)

if doInDetGlobalPrimaryVertexMonAlg:
  inDetGlobalPrimaryVertexMonAlg = helper.addAlgorithm(InDetGlobalPrimaryVertexMonAlg, 'InDetGlobalPrimaryVertexMonAlg')
  for k, v in kwargsInDetGlobalPrimaryVertexMonAlg.items():
      setattr(inDetGlobalPrimaryVertexMonAlg, k, v)

  InDetGlobalPrimaryVertexMonAlgCfg(helper, inDetGlobalPrimaryVertexMonAlg, **kwargsInDetGlobalPrimaryVertexMonAlg)


if doInDetGlobalBeamSpotMonAlg:
  inDetGlobalBeamSpotMonAlg = helper.addAlgorithm(InDetGlobalBeamSpotMonAlg, 'InDetGlobalBeamSpotMonAlg')
  for k, v in kwargsInDetGeamSpotMonAlg, k, v)
lobalBeamSpotMonAlg.items():
      setattr(inDetGlobalB
  InDetGlobalBeamSpotMonAlgCfg(helper, inDetGlobalBeamSpotMonAlg, **kwargsInDetGlobalBeamSpotMonAlg)


if doInDetGlobalLRTMonAlg:
  inDetGlobalLRTMonAlg = helper.addAlgorithm(InDetGlobalLRTMonAlg, 'InDetGlobalLRTMonAlg')
  for k, v in kwargsInDetGlobalLRTMonAlg.items():
      setattr(inDetGlobalLRTMonAlg, k, v)


  inDetGlobalLRTMonAlg.TrackSelectionTool.UseTrkTrackTools = True
  inDetGlobalLRTMonAlg.TrackSelectionTool.CutLevel         = "TightPrimary"
  inDetGlobalLRTMonAlg.TrackSelectionTool.maxNPixelHoles   = 1
  inDetGlobalLRTMonAlg.TrackSelectionTool.minPt            = 5000
  inDetGlobalLRTMonAlg.TrackSelectionTool.TrackSummaryTool = InDetTrackSummaryTool
  inDetGlobalLRTMonAlg.TrackSelectionTool.Extrapolator     = InDetExtrapolator


  InDetGlobalLRTonAlgCfg(helper, inDetGlobalTrackMonAlg, **kwargsInDetGlobalLRTMonAlg)


topSequence += helper.result()
