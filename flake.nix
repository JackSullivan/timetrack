{
  description = "Basic flake for multisystem nixpkgs";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem(system:
    let pkgs = nixpkgs.legacyPackages.${system};
    natlibpy = ps: ps.buildPythonPackage rec {
      pname = "natlibpy";
      version = "1.0.0";
      src = ps.fetchPypi {
        inherit pname version;
        sha256 = "sha256-6gOnl5aNNV6NfbfK+RLZguEoJNmcMf7SVcky/bexK64=";
      };
    };
    pyminder = ps: ps.buildPythonPackage rec {
      pname = "pyminder";
      version = "1.1.1";
      src = ps.fetchPypi {
        inherit pname version;
        sha256 = "sha256-AxplLYeCojrbK+Pb5+mHQe3mAKRcaLKyLW3MjVFCUGc=";
      };
      buildInputs = [ps.requests (natlibpy ps)];
    };
    python = pkgs.python311.withPackages(ps: with ps; [ (pyminder ps) ipython aw-client aw-core requests]);
    in {
      devShells.default = pkgs.mkShell {
        buildInputs = [python];
      };
      packages.default = python;
    }
  );
}
