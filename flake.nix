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
      my_presenterm-export = pkgs.python311Packages.buildPythonPackage rec {
        propagatedBuildInputs = with pkgs.python311Packages; [ setuptools ansi2html libtmux weasyprint dataclass-wizard ];
        pname = "presenterm-export";
        version = "0.2.2";
        format = "wheel";
        # src = /home/orahcio/Projetos/presenterm-export; 
        url = "https://files.pythonhosted.org/packages/d9/94/7446e2ca3a6a4f5f66acc50291115db06c440a803d0a19c18d614e0a22ba/presenterm_export-0.2.1-py3-none-any.whl";
        src = pkgs.fetchurl { #fetchPypi {
          inherit url; # pname version;
          sha256 = "74b687d4682095d31d3f85536f79a8061d80de10d08ab581f2460c5fd33a0dad";
        };
      };

      my_pyfxr = pkgs.python311Packages.buildPythonPackage rec {
        # propagatedBuildInputs = with pkgs.python311Packages; [ setuptools ];
        pname = "pyfxr";
        version = "0.3.0";
        format = "wheel";
        url = "https://files.pythonhosted.org/packages/83/f9/68ef33dcdfef32e9e479d209371d11b84ef561f3369694142a6212863761/pyfxr-0.3.0-pp310-pypy310_pp73-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl";
        src = pkgs.fetchPypi {
          inherit pname version;
          sha256 = "de997cb504f0e0fbe9a21f2174ea0a105a8748952521410e4691df7027876083";
        };
      };
      my_pgzero = pkgs.python311Packages.buildPythonPackage rec {
        propagatedBuildInputs = with pkgs.python311Packages; [ numpy pygame my_pyfxr ];
        pname = "pgzero";
        version = "1.2.1";
        format = "wheel";
        url = "https://files.pythonhosted.org/packages/2c/66/bc46c203802d47fa30a6caa92d13392274bcbebbb9ffcd0c5ed8030b3611/pgzero-1.2.1-py3-none-any.whl";
        src = pkgs.fetchurl {
          inherit url;
          sha256 = "734e1de1a99804c2610f90aa419411fc2b31200b9d683b6c9fc710c7a8e36606";
        };
      };
    in rec {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          # stdenv.cc.cc.lib
          # SDL2
          # xorg.libX11
          (python311.withPackages(ps: with ps; [
            pip
            ipykernel
            pygame
            my_pgzero
            my_presenterm-export
          ]))
          pandoc
          presenterm
          tmux
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
