# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..epi import Eddy


def test_Eddy_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        cnr_maps=dict(
            argstr='--cnr_maps',
            min_ver='5.0.10',
        ),
        dont_peas=dict(argstr='--dont_peas', ),
        dont_sep_offs_move=dict(argstr='--dont_sep_offs_move', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fep=dict(argstr='--fep', ),
        field=dict(argstr='--field=%s', ),
        field_mat=dict(
            argstr='--field_mat=%s',
            extensions=None,
        ),
        flm=dict(argstr='--flm=%s', ),
        fudge_factor=dict(
            argstr='--ff=%s',
            usedefault=True,
        ),
        fwhm=dict(argstr='--fwhm=%s', ),
        in_acqp=dict(
            argstr='--acqp=%s',
            extensions=None,
            mandatory=True,
        ),
        in_bval=dict(
            argstr='--bvals=%s',
            extensions=None,
            mandatory=True,
        ),
        in_bvec=dict(
            argstr='--bvecs=%s',
            extensions=None,
            mandatory=True,
        ),
        in_file=dict(
            argstr='--imain=%s',
            extensions=None,
            mandatory=True,
        ),
        in_index=dict(
            argstr='--index=%s',
            extensions=None,
            mandatory=True,
        ),
        in_mask=dict(
            argstr='--mask=%s',
            extensions=None,
            mandatory=True,
        ),
        in_topup_fieldcoef=dict(
            argstr='--topup=%s',
            extensions=None,
            requires=['in_topup_movpar'],
        ),
        in_topup_movpar=dict(
            extensions=None,
            requires=['in_topup_fieldcoef'],
        ),
        interp=dict(argstr='--interp=%s', ),
        is_shelled=dict(argstr='--data_is_shelled', ),
        method=dict(argstr='--resamp=%s', ),
        niter=dict(
            argstr='--niter=%s',
            usedefault=True,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        nvoxhp=dict(
            argstr='--nvoxhp=%s',
            usedefault=True,
        ),
        out_base=dict(
            argstr='--out=%s',
            usedefault=True,
        ),
        output_type=dict(),
        repol=dict(argstr='--repol', ),
        residuals=dict(
            argstr='--residuals',
            min_ver='5.0.10',
        ),
        session=dict(
            argstr='--session=%s',
            extensions=None,
        ),
        slm=dict(argstr='--slm=%s', ),
        use_cuda=dict(),
    )
    inputs = Eddy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Eddy_outputs():
    output_map = dict(
        out_cnr_maps=dict(extensions=None, ),
        out_corrected=dict(extensions=None, ),
        out_movement_rms=dict(extensions=None, ),
        out_outlier_report=dict(extensions=None, ),
        out_parameter=dict(extensions=None, ),
        out_residuals=dict(extensions=None, ),
        out_restricted_movement_rms=dict(extensions=None, ),
        out_rotated_bvecs=dict(extensions=None, ),
        out_shell_alignment_parameters=dict(extensions=None, ),
    )
    outputs = Eddy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
