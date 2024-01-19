Name:           python-trio-websocket
Version:        0.11.1
Release:        1
Summary:        WebSocket library for Trio
Group:          Development/Python

License:        MIT
URL:            https://github.com/python-trio/trio-websocket
Source:         https://files.pythonhosted.org/packages/source/t/trio-websocket/trio-websocket-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)

Requires:  python-trio
Requires:  python-wsproto

%description
This library implements both server and client aspects of the the WebSocket
protocol, striving for safety, correctness, and ergonomics. It is based on the
wsproto project, which is a Sans-IO state machine that implements the majority
of the WebSocket protocol, including framing, codecs, and events. This library
handles I/O using the Trio framework. This library passes the Autobahn Test
Suite.}

%prep
%autosetup -p1 -n trio-websocket-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSE
%{python_sitelib}/trio_websocket-%{version}-py*.*.egg-info
%{python_sitelib}/trio_websocket/
