# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brainsfit import BRAINSFit


def test_BRAINSFit_inputs():
    input_map = dict(
        ROIAutoClosingSize=dict(argstr='--ROIAutoClosingSize %f', ),
        ROIAutoDilateSize=dict(argstr='--ROIAutoDilateSize %f', ),
        args=dict(argstr='%s', ),
        backgroundFillValue=dict(argstr='--backgroundFillValue %f', ),
        bsplineTransform=dict(
            argstr='--bsplineTransform %s',
            hash_files=False,
        ),
        costFunctionConvergenceFactor=dict(
            argstr='--costFunctionConvergenceFactor %f', ),
        costMetric=dict(argstr='--costMetric %s', ),
        debugLevel=dict(argstr='--debugLevel %d', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        failureExitCode=dict(argstr='--failureExitCode %d', ),
        fixedBinaryVolume=dict(
            argstr='--fixedBinaryVolume %s',
            extensions=None,
        ),
        fixedVolume=dict(
            argstr='--fixedVolume %s',
            extensions=None,
        ),
        fixedVolume2=dict(
            argstr='--fixedVolume2 %s',
            extensions=None,
        ),
        fixedVolumeTimeIndex=dict(argstr='--fixedVolumeTimeIndex %d', ),
        gui=dict(argstr='--gui ', ),
        histogramMatch=dict(argstr='--histogramMatch ', ),
        initialTransform=dict(
            argstr='--initialTransform %s',
            extensions=None,
        ),
        initializeRegistrationByCurrentGenericTransform=dict(
            argstr='--initializeRegistrationByCurrentGenericTransform ', ),
        initializeTransformMode=dict(argstr='--initializeTransformMode %s', ),
        interpolationMode=dict(argstr='--interpolationMode %s', ),
        linearTransform=dict(
            argstr='--linearTransform %s',
            hash_files=False,
        ),
        logFileReport=dict(
            argstr='--logFileReport %s',
            hash_files=False,
        ),
        maskInferiorCutOffFromCenter=dict(
            argstr='--maskInferiorCutOffFromCenter %f', ),
        maskProcessingMode=dict(argstr='--maskProcessingMode %s', ),
        maxBSplineDisplacement=dict(argstr='--maxBSplineDisplacement %f', ),
        maximumNumberOfCorrections=dict(
            argstr='--maximumNumberOfCorrections %d', ),
        maximumNumberOfEvaluations=dict(
            argstr='--maximumNumberOfEvaluations %d', ),
        maximumStepLength=dict(argstr='--maximumStepLength %f', ),
        medianFilterSize=dict(
            argstr='--medianFilterSize %s',
            sep=',',
        ),
        metricSamplingStrategy=dict(argstr='--metricSamplingStrategy %s', ),
        minimumStepLength=dict(
            argstr='--minimumStepLength %s',
            sep=',',
        ),
        movingBinaryVolume=dict(
            argstr='--movingBinaryVolume %s',
            extensions=None,
        ),
        movingVolume=dict(
            argstr='--movingVolume %s',
            extensions=None,
        ),
        movingVolume2=dict(
            argstr='--movingVolume2 %s',
            extensions=None,
        ),
        movingVolumeTimeIndex=dict(argstr='--movingVolumeTimeIndex %d', ),
        numberOfHistogramBins=dict(argstr='--numberOfHistogramBins %d', ),
        numberOfIterations=dict(
            argstr='--numberOfIterations %s',
            sep=',',
        ),
        numberOfMatchPoints=dict(argstr='--numberOfMatchPoints %d', ),
        numberOfSamples=dict(argstr='--numberOfSamples %d', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputFixedVolumeROI=dict(
            argstr='--outputFixedVolumeROI %s',
            hash_files=False,
        ),
        outputMovingVolumeROI=dict(
            argstr='--outputMovingVolumeROI %s',
            hash_files=False,
        ),
        outputTransform=dict(
            argstr='--outputTransform %s',
            hash_files=False,
        ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        outputVolumePixelType=dict(argstr='--outputVolumePixelType %s', ),
        projectedGradientTolerance=dict(
            argstr='--projectedGradientTolerance %f', ),
        promptUser=dict(argstr='--promptUser ', ),
        relaxationFactor=dict(argstr='--relaxationFactor %f', ),
        removeIntensityOutliers=dict(argstr='--removeIntensityOutliers %f', ),
        reproportionScale=dict(argstr='--reproportionScale %f', ),
        samplingPercentage=dict(argstr='--samplingPercentage %f', ),
        scaleOutputValues=dict(argstr='--scaleOutputValues ', ),
        skewScale=dict(argstr='--skewScale %f', ),
        splineGridSize=dict(
            argstr='--splineGridSize %s',
            sep=',',
        ),
        strippedOutputTransform=dict(
            argstr='--strippedOutputTransform %s',
            hash_files=False,
        ),
        transformType=dict(
            argstr='--transformType %s',
            sep=',',
        ),
        translationScale=dict(argstr='--translationScale %f', ),
        useAffine=dict(argstr='--useAffine ', ),
        useBSpline=dict(argstr='--useBSpline ', ),
        useComposite=dict(argstr='--useComposite ', ),
        useROIBSpline=dict(argstr='--useROIBSpline ', ),
        useRigid=dict(argstr='--useRigid ', ),
        useScaleSkewVersor3D=dict(argstr='--useScaleSkewVersor3D ', ),
        useScaleVersor3D=dict(argstr='--useScaleVersor3D ', ),
        useSyN=dict(argstr='--useSyN ', ),
        writeOutputTransformInFloat=dict(
            argstr='--writeOutputTransformInFloat ', ),
        writeTransformOnFailure=dict(argstr='--writeTransformOnFailure ', ),
    )
    inputs = BRAINSFit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BRAINSFit_outputs():
    output_map = dict(
        bsplineTransform=dict(extensions=None, ),
        linearTransform=dict(extensions=None, ),
        logFileReport=dict(extensions=None, ),
        outputFixedVolumeROI=dict(extensions=None, ),
        outputMovingVolumeROI=dict(extensions=None, ),
        outputTransform=dict(extensions=None, ),
        outputVolume=dict(extensions=None, ),
        strippedOutputTransform=dict(extensions=None, ),
    )
    outputs = BRAINSFit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
