import nipype.interfaces.fsl as fsl
import os

from nipype.testing import *

# test Bet
def test_bet():
    better = fsl.Bet()
    yield assert_equal, better.cmd, 'bet'

    # Test raising error with mandatory args absent
    yield assert_raises, AttributeError, better.run

    # .inputs based parameter setting
    better.inputs.frac = 0.5
    better.inputs.infile = 'infile'
    better.inputs.outfile = 'outfile'
    yield assert_equal, better.cmdline, 'bet infile outfile -f 0.50'

    # .run() based parameter setting
    betted = better.run(infile='infile2', outfile='outfile')
    # Non-existant files, shouldn't finish cleanly
    yield assert_not_equal, betted.runtime.returncode, 0
    yield assert_equal, betted.interface.inputs.infile, 'infile2'
    yield assert_equal, betted.interface.inputs.outfile, 'outfile'
    yield assert_equal, betted.runtime.cmdline, 'bet infile2 outfile -f 0.50'
    
    # test that an outfile is autogenerated when inputs.outfile is None
    better.inputs.infile = 'infile'
    better.inputs.outfile = None
    allargs = better._parse_inputs()
    yield assert_equal, allargs[1], os.path.join(os.path.abspath('.'),'infile_bet')

    # Our options and some test values for them
    # Should parallel the opt_map structure in the class for clarity
    opt_map = {
        'outline':            ('-o', True),
        'mask':               ('-m', True),
        'skull':              ('-s', True),
        'nooutput':           ('-n', True),
        'frac':               ('-f 0.40', 0.4),
        'vertical_gradient':  ('-g 0.75', 0.75),
        'radius':             ('-r 20', 20),
        'center':             ('-c 54 75 80', (54, 75, 80)),
        'threshold':          ('-t', True),
        'mesh':               ('-e', True),
        'verbose':            ('-v', True),
        'flags':              ('--i-made-this-up', '--i-made-this-up'),
            }
    # Currently we don't test -R, -S, -B, -Z, -F, -A or -A2
    

    # test each of our arguments
    for name, settings in opt_map.items():
        better = fsl.Bet(**{name: settings[1]})
        # Could also test for containment, but that's less stringent
        yield assert_equal, super(fsl.Bet, better)._parse_inputs(), \
            [settings[0]]
    
        
# test fast
def test_fast():
    faster = fsl.Fast()
    faster.inputs.verbose = True
    fasted = faster.run(infiles='infile')
    fasted2 = faster.run(infiles=['infile', 'otherfile'])
    
    yield assert_equal, faster.cmd, 'fast'
    yield assert_equal, faster.inputs.verbose, True
    yield assert_equal, faster.inputs.manualseg , None
    yield assert_not_equal, faster, fasted
    yield assert_equal, fasted.runtime.cmdline, 'fast --verbose infile'
    yield assert_equal, fasted2.runtime.cmdline, 'fast --verbose infile otherfile'
   
    # Our options and some test values for them
    # Should parallel the opt_map structure in the class for clarity
    opt_map = {'number_classes':       ('--class 4', 4),
               'bias_iters':           ('--iter 5', 5),
               'bias_lowpass':         ('--lowpass 15', 15),
               'img_type':             ('--type 2', 2),
               'init_seg_smooth':      ('--fHard 0.035', 0.035),
               'segments':             ('--segments', True),
               'init_transform':       ('-a xform.mat', 'xform.mat'),
               'other_priors':         ('-A prior1.nii prior2.nii prior3.nii', 
                       ('prior1.nii', 'prior2.nii', 'prior3.nii')),
               'nopve':                ('--nopve', True),
               'output_biasfield':     ('-b', True),
               'output_biascorrected': ('-B', True),
               'nobias':               ('--nobias', True),
               'n_inputimages':        ('--channels 2', 2),
               'out_basename':         ('--out fasted', 'fasted'),
               'use_priors':           ('--Prior', True),
               'segment_iters':        ('--init 14', 14),
               'mixel_smooth':         ('--mixel 0.25', 0.25),
               'iters_afterbias':      ('--fixed 3', 3),
               'hyper':                ('--Hyper 0.15', 0.15),
               'verbose':              ('--verbose', True), 
               'manualseg':            ('--manualseg intensities.nii',
                       'intensities.nii'),
               'probability_maps':     ('-p', True),
              }
   
    # test each of our arguments
    for name, settings in opt_map.items():
        faster = fsl.Fast(**{name: settings[1]})
        # Could also test for containment, but that's less stringent
        yield assert_equal, super(fsl.Fast, faster)._parse_inputs(), \
                [settings[0]]

#test flirt
def test_flirt():
    flirter = fsl.Flirt()
    flirter.inputs.bins = 256
    flirter.inputs.cost = 'mutualinfo'
    flirted = flirter.run(infile='infile',reference='reffile',
                          outfile='outfile',outmatrix='outmat.mat')
    flirt_est = flirter.run(infile='infile',reference='reffile',
                            outfile=None,outmatrix='outmat.mat')
    flirt_apply = flirter.applyxfm(infile='infile',reference='reffile',
                                   inmatrix='inmatrix.mat',outfile='outimgfile')
    
    yield assert_not_equal, flirter, flirted
    yield assert_not_equal, flirted, flirt_est
    yield assert_not_equal, flirted, flirt_apply

    yield assert_equal, flirter.cmd, 'flirt'
    yield assert_equal, flirter.inputs.bins, flirted.interface.inputs.bins
    yield assert_equal, flirter.inputs.cost, flirt_est.interface.inputs.cost
    yield assert_equal, flirter.inputs.cost, flirt_apply.interface.inputs.cost
    yield assert_equal, flirt_apply.runtime.cmdline,'flirt -in infile -ref reffile -omat outmat.mat -init inmatrix.mat -out outimgfile -cost mutualinfo -applyxfm -bins 256'
    
#test fnirt
def test_fnirt():
    fnirt = fsl.Fnirt()
    fnirt.inputs.sub_sampling = [8,6,4]
    fnirt2 = fsl.Fnirt(sub_sampling=[8,2])
    fnirtd = fnirt.run(infile='infile', reference='reference')
    fnirtd2 = fnirt2.run(infile='infile', reference='reference')
    yield assert_equal, fnirt.cmd, 'fnirt'
    yield assert_equal, fnirt.inputs.sub_sampling, [8,6,4]
    yield assert_equal, fnirtd2.runtime.cmdline, 'fnirt --in=infile --ref=reference --subsample 8 2'
    yield assert_equal, fnirtd.runtime.cmdline,'fnirt --in=infile --ref=reference --subsample 8 6 4'
 
