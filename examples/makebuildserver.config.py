#!/usr/bin/env python3
#
# You may want to alter these before running ./makebuildserver

# In the process of setting up the build server, many gigs of files
# are downloaded (Android SDK components, gradle, etc).  These are
# cached so that they are not redownloaded each time. By default,
# these are stored in ~/.cache/fdroidserver
#
# cachedir = 'buildserver/cache'

# To specify which Debian mirror the build server VM should use, by
# default it uses http.debian.net, which auto-detects which is the
# best mirror to use.
#
# debian_mirror = 'http://ftp.uk.debian.org/debian/'

# The amount of RAM the build server will have (default: 2048)
# memory = 3584

# The number of CPUs the build server will have
# cpus = 1

# Debian package proxy server - if you have one
# aptproxy = "http://192.168.0.19:8000"

# If this is running on an older machine or on a virtualized system,
# it can run a lot slower. If the provisioning fails with a warning
# about the timeout, extend the timeout here. (default: 600 seconds)
#
# boot_timeout = 1200

# By default, this whole process uses VirtualBox as the provider, but
# QEMU+KVM is also supported via the libvirt plugin to vagrant. If
# this is run within a KVM guest, then libvirt's QEMU+KVM will be used
# automatically.  It can also be manually enabled by uncommenting
# below:
#
# vm_provider = 'libvirt'

# By default libvirt uses 'virtio' for both network and disk drivers.
# Some systems (eg. nesting VMware ESXi) do not support virtio. As a
# workaround for such rare cases, this setting allows to configure
# KVM/libvirt to emulate hardware rather than using virtio.
#
# libvirt_disk_bus = 'sata'
# libvirt_nic_model_type = 'rtl8139'

# Sometimes, it is not possible to use the 9p synced folder type with
# libvirt, like if running a KVM buildserver instance inside of a
# VMware ESXi guest.  In that case, using NFS or another method is
# required.
#
# synced_folder_type = 'nfs'
