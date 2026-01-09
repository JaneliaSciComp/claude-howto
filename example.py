#!/usr/bin/env python
"""Example script that fetches zarr metadata from a public S3 bucket."""

import s3fs

ZARR_PATH = "s3://janelia-cosem-datasets/jrc_mus-choroid-plexus-3/jrc_mus-choroid-plexus-3.zarr"


def main():
    print(f"Fetching metadata from {ZARR_PATH}")

    fs = s3fs.S3FileSystem(anon=True)

    # List top-level contents
    contents = fs.ls(ZARR_PATH)
    print(f"\nTop-level contents ({len(contents)} items):")
    for item in contents[:10]:
        name = item.split("/")[-1]
        print(f"  {name}")
    if len(contents) > 10:
        print(f"  ... and {len(contents) - 10} more")

    # Read the root .zattrs metadata
    zattrs_path = f"{ZARR_PATH}/.zattrs"
    if fs.exists(zattrs_path):
        import json

        with fs.open(zattrs_path) as f:
            attrs = json.load(f)
        print(f"\nRoot attributes:")
        for key, value in list(attrs.items())[:5]:
            print(f"  {key}: {value}")

    # Open a specific multiscale array and show its shape
    # This dataset uses OME-NGFF format with recon-1/em/fibsem-uint8 path
    array_path = f"{ZARR_PATH}/recon-1/em/fibsem-uint8/s0"
    zarray_path = f"{array_path}/.zarray"
    if fs.exists(zarray_path):
        import json

        with fs.open(zarray_path) as f:
            arr_meta = json.load(f)
        print(f"\nArray at recon-1/em/fibsem-uint8/s0:")
        print(f"  shape: {arr_meta.get('shape')}")
        print(f"  dtype: {arr_meta.get('dtype')}")
        print(f"  chunks: {arr_meta.get('chunks')}")


if __name__ == "__main__":
    main()
