{
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-unstable";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };
  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
      pgzero = pkgs.python3Packages.buildPythonPackage rec {
        propagatedBuildInputs = with pkgs.python3Packages;[
          pygame
        ];
        pname = "pgzero";
        version = "1.2.1";
        format = "wheel";
        url = "https://files.pythonhosted.org/packages/2c/66/bc46c203802d47fa30a6caa92d13392274bcbebbb9ffcd0c5ed8030b3611/pgzero-1.2.1-py3-none-any.whl";
        src = pkgs.fetchurl { # pkgs.python311Packages.fetchPypi {
          inherit url; # pname version;
          sha256 = "734e1de1a99804c2610f90aa419411fc2b31200b9d683b6c9fc710c7a8e36606";
        };
      };
    in rec {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          # stdenv.cc.cc.lib
          # SDL2
          # xorg.libX11
          (python3.withPackages(ps: with ps; [
            pip
            jupyter
            jupyterlab
            pygame
            pgzero
          ]))
          pandoc
          # virtualenv
        ];
        shellHook = ''
          # export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib/:${pkgs.xorg.libX11}/lib
          # export PIP_PREFIX=$(pwd)/_build/pip_packages #Dir where built packages are stored
          # export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
          # export PATH="$PIP_PREFIX/bin:$PATH"
          # unset SOURCE_DATE_EPOCH
          # source .venv/bin/activate
        '';
      };
    }
  );
}
