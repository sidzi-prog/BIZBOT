# BizBot

A modular, configurable business management platform built with Python.

## Overview

BizBot is designed to provide a shared foundation for managing multiple businesses through messaging platforms.

The project aims to support different business types using a modular architecture, allowing each business to use common features and business-specific functionality.

## Planned Features

- Multi-business management
- User and membership management
- Role-based access control (RBAC)
- Customer management
- Business-specific modules
- Request and order management
- Administrative reports
- Database integration

## Technology Stack

- Python 3.12+
- SQLite (planned)
- Telegram Bot API (planned)
- Pytest

## Project Structure

The project follows a `src`-based Python package layout.

## Project Status

**Under Development**

The initial domain models, including `Business` and `User`, have been implemented. Core architecture and additional features are under development.


## Roadmap

### Core Architecture
- [x] Business domain model
- [x] User domain model
- [x] Initial input validation
- [x] UUID-based identifiers
- [x] Basic activation state management
- [x] Initial pytest coverage

### Planned Features
- [ ] UserAccount and authentication management
- [ ] UserIdentity for messaging platform integrations
- [ ] BusinessMembership for multi-business relationships
- [ ] Role-Based Access Control (RBAC)
- [ ] Contact information management
- [ ] Customer management
- [ ] Database integration
- [ ] Telegram and Bale integrations
