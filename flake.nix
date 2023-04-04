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
    in rec {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          # stdenv.cc.cc.lib
          # SDL2
          # xorg.libX11
          (python3.withPackages(ps: with ps; [
            jupyter
            pygame
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
