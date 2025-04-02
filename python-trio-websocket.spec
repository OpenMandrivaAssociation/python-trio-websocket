%define module trio-websocket
%define uname trio_websocket

Name:           python-trio-websocket
Version:        0.12.2
Release:        1
Summary:        WebSocket library for Trio
Group:          Development/Python
License:        MIT
URL:            https://github.com/python-trio/trio-websocket
Source:         https://files.pythonhosted.org/packages/source/t/trio-websocket/%{uname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(pip)

Requires:  python%{pyver}dist(trio)
Requires:  python%{pyver}dist(wsproto)
Requires:  python%{pyver}dist(outcome)

%description
This library implements both server and client aspects of the the WebSocket
protocol, striving for safety, correctness, and ergonomics. It is based on the
wsproto project, which is a Sans-IO state machine that implements the majority
of the WebSocket protocol, including framing, codecs, and events. This library
handles I/O using the Trio framework. This library passes the Autobahn Test
Suite.}

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/%{uname}-%{version}.dist-info
%{python_sitelib}/%{uname}
%doc README.md
%license LICENSE
